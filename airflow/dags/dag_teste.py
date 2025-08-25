from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys, os

# sys.path.insert(0, '/src')
# sys.path.insert(0, '/opt/airflow/src')
# sys.path.insert(0, os.path.join('/opt/airflow', 'src'))

# Adiciona /src no sys.path para importar seu módulo

from src.automations.callix.callix_subaccount_scrap import enviar_dados_api  # ajuste o nome do módulo conforme arquivo real

# with DAG(
#     dag_id="executar_automacao",
#     start_date=datetime(2025, 7, 3),
#     schedule="0 0 * * *",  # ou cron
#     catchup=False,
# ) as dag:
#     executar = PythonOperator(
#         task_id="executar_enviar_dados_api",
#         python_callable=enviar_dados_api
#     )