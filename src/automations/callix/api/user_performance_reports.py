import requests
import datetime
from src.core.storage_saver import save_json_to_gcs

def get_user_performance_reports(subdomain, token):
    #token = (Logica pra pegar o token dentro do banco de dados, se não existir, levantar uma exceção pra colocarmos manualmente la)

    subdomain = f"https://{subdomain}.callix.com.br/api/v1/user_performance_reports"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    today = datetime.date.today()
    today_formatted = today.strftime("%Y-%m-%d")

    tomorrow = today + datetime.timedelta(days=1)
    tomorrow_formatted = tomorrow.strftime("%Y-%m-%d")

    querystring = {
        "filter[date]":
            f"{today_formatted}T00:00:00.000Z,"
            f"{tomorrow_formatted}T23:59:59.999Z"
    }

    r = requests.get(url=subdomain, headers=headers, params=querystring)
    response = r.json()
    print(r.status_code)
    return response



if __name__ == "__main__":
    subdomain = 'rdfcontech'
    token = 'c43c806e-9bfc-4a8e-8464-96ee11501cae'
    resposta = fetch_user_performance_reports(subdomain=subdomain, token=token)
    print(resposta)

    save_json_to_gcs(
        bucket_name="jamesia_datalake",
        module="callix",
        endpoint="outgoing_call_summaries",
        data=resposta
    )
