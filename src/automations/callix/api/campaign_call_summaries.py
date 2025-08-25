import requests

def fetch_campaign_call_summaries(route, domain, token, start_date, end_date):
    endpoint = f"https://{domain}.callix.com.br/api/v1/campaign_call_summaries"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    querystring = {
        "filter[date]": f"{start_date}T00:00:00.000Z,{end_date}T23:59:59.999Z"
    }

    response = requests.get(url=endpoint, headers=headers, params=querystring)
    response.raise_for_status()

    return response.json()