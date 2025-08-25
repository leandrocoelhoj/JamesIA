import psycopg2
from src.db.connection import DB_CONFIG

def get_envs_with_token():
    results = []
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT DISTINCT ON (ec.dominio) ec.dominio, st.token
                FROM automacao_subdominiotokens st
                JOIN automacao_empresascallix ec
                  ON ec.id = st.equipe_fk_id
                WHERE ec.status IN ('Ativo', 'Teste')
                ORDER BY ec.dominio, st.id
            """)
            for dominio, token in cur.fetchall():
                results.append({"dominio": dominio, "token": token})
    return results

def get_active_envs_without_token():
    results = []
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                    SELECT id, dominio
                    FROM automacao_empresascallix
                    WHERE status IN ('Ativo', 'Teste')
                      AND id NOT IN (
                          SELECT DISTINCT equipe_fk_id
                          FROM automacao_subdominiotokens
                      )
                """)
            for equipe_id, dominio in cur.fetchall():
                results.append({"equipe_id": equipe_id, "dominio": dominio})
    return results

def insert_token_to_db(equipe_id, token):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO automacao_subdominiotokens (equipe_fk_id, token) VALUES (%s, %s)",
                (equipe_id, token)
            )
            conn.commit()



def get_equipe_id_by_domain(dominio):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id FROM automacao_empresascallix WHERE dominio = %s",
                (dominio,)
            )
            row = cur.fetchone()
            if row:
                return row[0]
            else:
                raise ValueError(f"Nenhum equipe encontrada para domínio '{dominio}'")

if __name__ == '__main__':
    print(get_active_envs_without_token())
