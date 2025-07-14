from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.automations.callix.api.admin.sub_accounts import get_sub_accounts_api
from src.core.storage_saver import save_json_to_gcs


def extract_callable(**kwargs):
    response = get_sub_accounts_api()
    kwargs['ti'].xcom_push(key='subaccounts_data', value=response)

def load_callable(**kwargs):
    data = kwargs['ti'].xcom_pull(key='subaccounts_data', task_ids='extract_subaccount')

    bucket_name = "jamesia_datalake"
    module = "callix"
    endpoint = "outgoing_call_summaries"

    save_json_to_gcs(bucket_name=bucket_name, module=module, endpoint=endpoint, data=data)

with DAG(
    dag_id="callix_subaccounts_lake",
    start_date=datetime(2025, 7, 3),
    schedule= "@daily",
    catchup=False,
) as dag:

    extract = PythonOperator(
        task_id="extract_subaccount",
        python_callable=extract_callable,
    )

    load = PythonOperator(
        task_id="load_subaccounts_to_lake",
        python_callable=load_callable,
    )

    extract >> load