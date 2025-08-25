import requests
import json

routes = ['user_performance_reports', 'campaign_call_summaries', 'outgoing_call_summaries']

def get_api_callix_data(endpoint, domain, token, start_date, end_date):
    print(f"[API GET CALLIX] REGISTROS: Dominio:{domain}, Token: {token}.")
    url = f"https://{domain}.callix.com.br/api/v1/{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    querystring = {
        "filter[date]": f"{start_date}T00:00:00.000Z,{end_date}T23:59:59.999Z"
    }
    response = requests.get(url=url, headers=headers, params=querystring)
    response.raise_for_status()
    return response.json()

def post_to_backend(endpoint, data, dominio):
    api_url = f"http://host.docker.internal:8000/api/callix_data/{endpoint}/"
    mapped_data = map_data(data=data, dominio=dominio, endpoint=endpoint)

    if not mapped_data:
        print(f"[API POST] payload vazio para {endpoint} | {dominio} — pulando POST.")
        return {"skipped": True, "count": 0}

    print(f"[API POST] Enviando {len(mapped_data)} registros para o endpoint {endpoint}.")

    r = requests.post(api_url, json=mapped_data)
    try:
        resp_body = r.json()
    except Exception:
        resp_body = r.text
    if r.status_code >= 400:
        print(f"[API POST] Falha ao enviar dados do endpoint {endpoint}: {r.status_code} {resp_body}")
    else:
        print(f"[API POST] Sucesso ao enviar dados do endpoint {endpoint} para API. Status: {r.status_code}")
    r.raise_for_status()
    return resp_body

def map_data(endpoint, data, dominio):
    mapped = []

    def attach_common(d):
        d['equipe'] = dominio
        return d

    if isinstance(data, list):
        for d in data:
            d = attach_common(d)
            if endpoint == 'user_performance_reports' and 'id' in d:
                d['operador_id'] = str(d['id'])
            mapped.append(d)
        return mapped

    # dict sem "data"
    if isinstance(data, dict) and 'data' not in data:
        data = attach_common(data)
        if endpoint == 'user_performance_reports' and 'id' in data:
            data['operador_id'] = str(data['id'])
        mapped.append(data)
        return mapped

    # {"data":[...]} (formato Callix)
    for item in data.get('data', []):
        attrs = (item.get('attributes') or {}).copy()
        attrs = attach_common(attrs)
        if endpoint == 'user_performance_reports' and 'id' in item:
            attrs['operador_id'] = str(item['id'])
        mapped.append(attrs)
    return mapped