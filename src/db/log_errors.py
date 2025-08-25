import psycopg2
from .connection import DB_CONFIG
from datetime import datetime

def log_falha(dominio, erro):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO log_processamento_callix (dominio, erro, datahora, status)
                VALUES (%s, %s, %s, 'falha')
            """, (dominio, str(erro), datetime.now()))
            conn.commit()
            cur.close()
            conn.close()