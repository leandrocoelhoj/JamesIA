from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from selenium import webdriver
from src.core.selenium_utils import get_chrome_driver
import logging

from src.automations.callix.callix_edit import scrap_and_save_token, scrap_domains_to_db
from src.db.get_from_db import get_active_envs_without_token, get_envs_with_token
from src.db.log_errors import log_falha
from src.automations.callix.api.requestions import get_api_callix_data, post_to_backend
from src.automations.callix.api.admin.sub_accounts import scrap_domains_api_db
from src.core.storage_saver import save_json_to_gcs

routes = ['user_performance_reports', 'campaign_call_summaries', 'outgoing_call_summaries']
BUCKET_NAME = "jamesia_datalake"
MODULE = "callix"

def fetch_subdomain_data_api():
    logging.info("Iniciando fetch_subdomains_data via API (scraping dos subdomínios)")
    response = scrap_domains_api_db()
    return response

def fetch_subdomains_data():
    logging.info("Iniciando fetch_subdomains_data (scraping dos subdomínios)")
    driver = get_chrome_driver()
    try:
        r = scrap_domains_to_db(driver)
        logging.info(f"Dados de subdomínios obtidos com sucesso. Total: {len(r)}")
        return r
    except Exception as e:
        logging.error(f"Erro ao executar fetch_subdomains_data: {e}")
        raise
    finally:
        driver.quit()
        if hasattr(driver, "_tmp_profile"):
            driver._tmp_profile.cleanup()

def prepare_tokens(**kwargs):
    missing_tokens = get_active_envs_without_token()
    for item in missing_tokens:
        equipe_id = item["equipe_id"]
        dominio = item["dominio"]
        driver = get_chrome_driver()
        try:
            token = scrap_and_save_token(driver, dominio)
            print(f"Token coletado e salvo para {equipe_id}:{dominio}\n {token}")
        except Exception as e:
            log_falha(dominio, f"SCRAP_TOKEN_FAIL: {e}")
        finally:
            driver.quit()
            if hasattr(driver, "_tmp_profile"):
                driver._tmp_profile.cleanup()

def prepare_routes(**kwargs):
    ...

def extract_and_load_group(envs_group, start_date, end_date, **kwargs):
    for envs in envs_group:
        dominio = envs['dominio']
        token = envs['token']
        # dominio = "rdfcontech"
        # token = "c43c806e-9bfc-4a8e-8464-96ee11501cae"
        for endpoint in routes:
            try:
                data = get_api_callix_data(endpoint, dominio, token, start_date, end_date)
                save_json_to_gcs(
                    bucket_name=BUCKET_NAME,
                    module=MODULE,
                    endpoint=endpoint,
                    domain=dominio,
                    data=data,
                    date_str=start_date
                )

                if endpoint == 'user_performance_reports' and isinstance(data, dict):
                    registros = data.get("data", [])
                    payload = []
                    for r in registros:
                        attrs = (r.get("attributes") or {}).copy()
                        op_id = r.get("id") or attrs.get("user_id") or attrs.get("operator_id")
                        if not op_id:
                            logging.warning("Sem operador_id: dominio=%s item=%s", dominio, r)
                            continue

                        attrs["operador_id"] = str(op_id)
                        attrs["equipe"] = dominio
                        payload.append(attrs)

                        if not payload:
                            print(f"[API POST] Nenhum registro para {endpoint} | {dominio}.")
                            continue

                    post_to_backend(endpoint, payload, dominio)

                else:
                    post_to_backend(endpoint, data, dominio)
                print(f"Sucesso: {dominio} | {endpoint}")
            except Exception as e:
                print(f"Erro em {dominio} ({endpoint}): {e}")
                #log_falha(dominio, f"{endpoint}: {e}")

def divide_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def fetch_and_shard_envs_with_token(**kwargs):
    envs = get_envs_with_token()  # List of {"dominio": "", "token" : ""}
    groups = list(divide_chunks(envs, 20))
    kwargs['ti'].xcom_push(key='env_groups', value=groups)

def dynamic_group_tasks(**kwargs):
    ti = kwargs['ti']
    start_date = ti.xcom_pull(key='start_date', task_ids='prepare_dates')
    end_date = ti.xcom_pull(key='end_date', task_ids='prepare_dates')
    groups = ti.xcom_pull(key='env_groups', task_ids='fetch_and_shard_envs_with_token')

    for idx, group in enumerate(groups):
        extract_and_load_group(
            envs_group=group,
            start_date=start_date,
            end_date=end_date
        )
    # for idx, group in enumerate(groups):
    #     extract_and_load_group(
    #         envs_group=group,
    #         start_date=start_date,
    #         end_date=end_date
    #     )
        # task = PythonOperator(
        #     task_id=f"extract_load_group_{idx}",
        #     python_callable=extract_and_load_group,
        #     op_kwargs={
        #         "envs_group": group,
        #         "start_date": start_date,
        #         "end_date": end_date
        #     },
        #     dag=kwargs['dag']
        # )
        # task.execute(kwargs)

with DAG(
    dag_id="callix_full_etl",
    start_date=datetime(2025, 7, 3),
    schedule="0 12 * * 2-7",
    catchup=False,
) as dag:

    def get_dates(ds, **kwargs):
        exec_date = datetime.strptime(ds, "%Y-%m-%d")

        target_date = exec_date - timedelta(days=1)
        start_date = target_date.strftime("%Y-%m-%d")
        end_date = exec_date.strftime("%Y-%m-%d")
        kwargs['ti'].xcom_push(key='start_date', value=start_date)
        kwargs['ti'].xcom_push(key='end_date', value=end_date)

    fetch_subdomains_data_task = PythonOperator(
        task_id="fetch_subdomains_data",
        python_callable=fetch_subdomain_data_api,
    )

    prepare_dates = PythonOperator(
        task_id="prepare_dates",
        python_callable=get_dates
    )

    prepare_tokens_task = PythonOperator(
        task_id="prepare_tokens",
        python_callable=prepare_tokens
    )

    fetch_envs_with_token = PythonOperator(
        task_id="fetch_and_shard_envs_with_token",
        python_callable=fetch_and_shard_envs_with_token,
    )

    process_groups = PythonOperator(
        task_id="process_groups",
        python_callable=dynamic_group_tasks,
    )

    [fetch_subdomains_data_task, prepare_dates] >> prepare_tokens_task >> fetch_envs_with_token >> process_groups