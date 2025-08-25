import requests
import os
from dotenv import load_dotenv
import logging

BASE_URL = f"http://host.docker.internal:8000/api"
load_dotenv()
def get_sub_accounts_api():
    full_url = f"https://contechsystem.callix.com.br/api/v1/sub_accounts?page[limit]=1500"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv("CONTECH_TOKEN")}"
    }

    try:
        r = requests.get(url=full_url, headers=headers)

        r.raise_for_status()

        response = r.json()
        domains_list = []

        for e in response['data']:
            status_pt = traduzir_status(e['attributes']['status'])
            domain_info = {
                "equipe": e['attributes']['name'],
                "dominio": e['attributes']['subdomain'],
                "status": status_pt,
                "pas": e['attributes']['max_simultaneous_web_access'],
                "ramais": e['attributes']['max_extensions'],
                "data-entrada": e['attributes']['entry_date']
            }

            domains_list.append(domain_info)

        return domains_list

    except requests.exceptions.RequestException as e:
        print("🚨 Erro na requisição:", e)
        raise Exception(f"Erro ao acessar API Callix: {e}")

def scrap_domains_api_db():
    logging.info(f"Coletando domínios via API...")
    try:
        domains_list = get_sub_accounts_api()
        logging.info(f"{len(domains_list)} domínios capturados. Enviando para API interna...")

        resp = requests.post(f"{BASE_URL}/callix-info/", json=domains_list)
        logging.info(f"Empresas enviadas para API interna. Status: {resp.status_code}")

        try:
            resp_data = resp.json()
            logging.info(f"Resposta detalhada da API interna: {resp_data}")
        except Exception as e:
            logging.error(f"Erro ao converter resposta da API para JSON: {e}\nTexto: {resp.text}")

        return domains_list
    except Exception as e:
        logging.error(f"Falha ao enviar empresas para API: {e}")
        return []

def traduzir_status(status):
    mapping = {
        "active": "Ativo",
        "inactive": "Inativo",
        "test": "Teste",
    }
    return mapping.get(status.lower(), status)