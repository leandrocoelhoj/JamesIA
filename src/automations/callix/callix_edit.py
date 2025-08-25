from src.pages.callix.api_tokens import TokenApiPage
from src.pages.callix.campaigns import CampaignPage
from src.pages.callix.users import UserPage
from src.pages.callix.account_data import AccountDataPage
from src.auth.factory import authenticate_system
from src.pages.callix.admin_page.sub_account_management import SubAccountPage
from src.db.get_from_db import insert_token_to_db, get_equipe_id_by_domain
from time import sleep
from selenium import webdriver
import json
import requests
from datetime import datetime
import logging

BASE_URL = f"http://host.docker.internal:8000/api"



def scrap_domains_to_db(driver):
    team_name = 'contechsystem'
    logging.info(f"Autenticando no sistema: {team_name}")
    config = authenticate_system(system='callix', team_name=team_name, driver=driver)
    logging.info(f"Autenticação realizada para {team_name}")
    sub_accounts_page = SubAccountPage(config, driver)
    domains_list = sub_accounts_page.get_domains()
    logging.info(f"{len(domains_list)} domínios capturados. Enviando para API...")

    try:
        resp = requests.post(f"{BASE_URL}/callix-info/", json=domains_list)
        logging.info(f"Empresas enviadas para API. Status: {resp.status_code}")
    except Exception as e:
        logging.error(f"Falha ao enviar empresas para API: {e}")
    return domains_list

def create_single_user(driver, users_name):
    domains_list1 = scrap_domains_to_db(driver)
    #driver = webdriver.Chrome()
    for domain in domains_list1:
        domain_name = domain.get("dominio")

        try:
            config2 = authenticate_system(system='callix', team_name=domain_name, driver=driver)
            user_page = UserPage(config2, driver)
            for user in users_name:
                user_page.create_adm_user()
                user_page.update_all_passwords(user, 0)
                sleep(0.5)

        except:
            print(f'Não foi possível acessar o ambiente: {domain_name}')
            continue

def scrap_route_and_agress(driver):
    empresas_payload = []
    campanhas_payload = []
    tokens_payload = []
    routes_payload = []

    equipes_info = {}

    domains_list = scrap_domains_to_db(driver)

    for domain in domains_list:
        equipe = domain.get("equipe")
        dominio = domain.get("dominio")
        status = domain.get("status")
        pas = domain.get("pas")
        ramais = domain.get("ramais")
        data_entrada = domain.get("data-entrada")


        empresas_payload.append({
            "equipe": equipe,
            "dominio": dominio,
            "status": status,
            "qtd_usuarios": pas,
            "qtd_ramais": ramais,
            "data-entrada": data_entrada
        })


        try:
            config2 = authenticate_system(system='callix', team_name=dominio, driver=driver)
            campaign_page = CampaignPage(config2, driver)
            account_data = AccountDataPage(config2, driver)
            token_api = TokenApiPage(config2, driver)

            #campaigns = campaign_page.scrap_campaigns()
            route = account_data.read_route()
            #token = token_api.read_tokens()

            # for campaign in campaigns:
            #     campanhas_payload.append({
            #         "equipe": equipe,
            #         "nome_campanha": campaign.get('campaign_name'),
            #         "agressividade": campaign.get('campaign_agress')
            #     })
            #
            # tokens_payload.append({
            #     "equipe": equipe,
            #     "token": token
            # })

            routes_payload.append({
                "equipe": equipe,
                "route": route
            })

            # campanhas_formatadas = [
            #     {
            #         "nome_campanha": c.get('campaign_name'),
            #         "agressividade": c.get('campaign_agress')
            #     } for c in campaigns
            # ]
            # equipes_info[equipe] = {
            #     "dominio": dominio,
            #     "status": status,
            #     "pas": pas,
            #     "ramais": ramais,
            #     "data-entrada": data_entrada,
            #     "campanhas": campanhas_formatadas,
            #     "token": token,
            #     "route": route
            # }

        except Exception as e:
            print(f"Houve falha no scrap do ambiente: {dominio}")
            continue

    print(json.dumps(equipes_info, indent=2, ensure_ascii=False))

    return {
        "empresas": empresas_payload,
        "campanhas": campanhas_payload,
        "tokens": tokens_payload,
        "routes": routes_payload,
        "debug_agrupado": equipes_info
    }

def enviar_payloads(scrap):
    log_envio = {
        "empresas": [],
        "campanhas": [],
        "tokens": [],
        "falhas": []
    }

    try:
        resp = requests.post(f"{BASE_URL}/callix-info/", json=scrap["empresas"])
        log_envio["empresas"].append({
            "status": resp.status_code,
            "response": resp.text
        })
        print(f"Empresas: {resp.status_code}")
    except Exception as e:
        log_envio["falhas"].append({"tipo": "empresas", "erro": str(e)})
        print(f"Falha ao enviar empresas: {e}")

    try:
        resp = requests.post(f"{BASE_URL}/campanhas/", json=scrap["campanhas"])
        log_envio["campanhas"].append({
            "status": resp.status_code,
            "response": resp.text
        })
        print(f"Campanhas: {resp.status_code}")
    except Exception as e:
        log_envio["falhas"].append({"tipo": "campanhas", "erro": str(e)})
        print(f"Falha ao enviar campanhas: {e}")

    for token_payload in scrap["tokens"]:
        try:
            resp = requests.post(f"{BASE_URL}/tokens/", json=token_payload)
            log_envio["tokens"].append({
                "equipe": token_payload["equipe"],
                "status": resp.status_code,
                "response": resp.text
            })
            print(f"Token {token_payload['equipe']}: {resp.status_code}")
        except Exception as e:
            log_envio["falhas"].append({"tipo": "token", "equipe": token_payload["equipe"], "erro": str(e)})
            print(f"Falha ao enviar token {token_payload['equipe']}: {e}")


    agora = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"log_envio_{agora}.json", "w", encoding="utf-8") as f:
        json.dump(log_envio, f, ensure_ascii=False, indent=2)
    print(f"Log salvo em log_envio_{agora}.json")


def scrap_and_save_token(driver, domain):
    try:
        logging.info(f"Iniciando scrap do token para domínio: {domain}")
        equipe_id = get_equipe_id_by_domain(domain)
        logging.info(f"ID da equipe obtido: {equipe_id} para domínio {domain}")

        config2 = authenticate_system(system='callix', team_name=domain, driver=driver)
        token_api = TokenApiPage(config2, driver)
        token = token_api.read_tokens()
        logging.info(f"Token(s) lido(s) da tela: {token} para domínio {domain}")

        if isinstance(token, list):
            single_token = token[0]
        else:
            single_token = token

        logging.info(f"Inserindo token no banco: equipe_id={equipe_id}, token={single_token}")

        insert_token_to_db(equipe_id, single_token)

        logging.info(f"Token coletado e salvo para {equipe_id}:{domain}: {single_token}")
        return single_token

    except Exception as e:
        logging.error(f"Erro ao coletar/salvar token para equipe {domain}: {e}", exc_info=True)
        return None

if __name__ == '__main__':
    driver = webdriver.Chrome()
    #teste = scrap_and_save_token(driver, 'simcontech')
    #print(teste)

    scrap = scrap_route_and_agress(driver)
    #enviar_payloads(scrap)
    print(scrap)
    input('=== CODIGO FINALIZADO ===')

    # driver = webdriver.Chrome()
    # #domains = domains(driver)
    # domains_lista = [{'domain': 'Contech - aguiacontech', 'domain_link': 'aguiacontech', 'status': 'Ativo', 'pas': '1', 'ramais': '0', 'data-entrada': '03/05/2024'}]
    # scrap = scrap_route_and_agress(driver, domains_lista)
    # print(scrap)
    # input()





