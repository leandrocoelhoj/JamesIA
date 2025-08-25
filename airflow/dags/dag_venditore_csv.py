from datetime import datetime, timedelta
import logging
import requests

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.exceptions import AirflowException

from src.automations.venditore.venditore_csv import parse_csv_custos
from src.automations.venditore.venditore_drive_gcp import (
    build_drive_client, find_folders, get_target_filename, download_drive_file_to_temp
)

BACKEND_BASE_URL = "http://jamesback:8000"

def _dates_to_fetch(exec_date: datetime.date):
    """Seg-Sex: regra especial na segunda; demais dias D-1."""
    wd = exec_date.weekday()
    if wd == 0:
        return [exec_date - timedelta(days=3),
                exec_date - timedelta(days=2)]
    return [exec_date - timedelta(days=1)]

def ingest_custos_task(ds, **_):
    exec_date = datetime.strptime(ds, "%Y-%m-%d").date()
    target_dates = _dates_to_fetch(exec_date)

    drive = build_drive_client()
    files = find_folders(drive)
    logging.info(f"Itens listados no Drive: {len(files)}")

    missing = []

    for d in target_dates:
        dd_mm_yyyy = d.strftime("%d-%m-%Y")
        yyyy_mm_dd = d.strftime("%Y-%m-%d")
        target_name = f"custos{dd_mm_yyyy}.csv"
        logging.info(f"[{yyyy_mm_dd}] procurando: {target_name}")

        venditore_file = get_target_filename(files, yyyy_mm_dd)
        if not venditore_file:
            logging.error(f"[{yyyy_mm_dd}] arquivo NÃO encontrado: {target_name}")
            missing.append(yyyy_mm_dd)
            continue

        tmp_csv = download_drive_file_to_temp(drive, venditore_file["id"])
        logging.info(f"[{yyyy_mm_dd}] CSV baixado: {tmp_csv}")

        csv_info = parse_csv_custos(tmp_csv, data_arquivo=yyyy_mm_dd)
        if not csv_info:
            logging.error(f"[{yyyy_mm_dd}] CSV vazio em {target_name}")
            missing.append(yyyy_mm_dd)
            continue

        r = requests.post(f"{BACKEND_BASE_URL}/api/ingest_custos/", json=csv_info, timeout=60)
        body = None
        try:
            body = r.json()
        except Exception:
            body = r.text
        logging.info(f"[{yyyy_mm_dd}] POST status={r.status_code} body={str(body)[:500]}")
        r.raise_for_status()

    if missing:
        raise AirflowException(f"Arquivos ausentes/CSV vazio para datas: {', '.join(missing)}")

    return {"run_date": exec_date.isoformat(), "processed": [d.strftime('%Y-%m-%d') for d in target_dates]}

with DAG(
    dag_id="venditore_ingest_custos",
    start_date=datetime(2025, 8, 1),
    schedule="0 7 * * *",
    catchup=False,
    tags=["venditore", "drive", "csv"],
) as dag:
    ingest = PythonOperator(
        task_id="ingest_custos_d_minus_logic",
        python_callable=ingest_custos_task,
    )