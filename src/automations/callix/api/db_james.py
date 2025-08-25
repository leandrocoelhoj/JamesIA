import psycopg2

def get_domains_and_tokens():
    conn = psycopg2.connect(
        host='localhost',
        database='devjames',
        user='postgres',
        password='1234'
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT DISTINCT ON (equipe_fk_id) equipe_fk_id, token
        FROM automacao_subdominiotokens
        ORDER BY equipe_fk_id, id
        """)
    # Pegando domínio pelo id da equipe (você pode precisar de JOIN ou SELECT extra)
    results = []
    for equipe_fk_id, token in cur.fetchall():
        cur2 = conn.cursor()
        cur2.execute("SELECT dominio FROM automacao_empresascallix WHERE id = %s", (equipe_fk_id,))
        dominio = cur2.fetchone()[0]
        results.append({"dominio": dominio, "token": token})
    cur.close()
    conn.close()
    return results

if __name__ == '__main__':
    result = get_domains_and_tokens()
    print(result)