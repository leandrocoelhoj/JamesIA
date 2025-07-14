import requests

def get_sub_accounts_api():
    url = 'contechsystem'
    token = '1fd9b913-e584-4763-a265-8aea1a236d43'

    full_url = f"https://{url}.callix.com.br/api/v1/sub_accounts"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    print("🔗 URL:", full_url)
    print("🔐 Headers:", headers)

    try:
        r = requests.get(url=full_url, headers=headers)
        print("📡 Status Code:", r.status_code)
        print("🧾 Raw Response Text:", r.text)

        r.raise_for_status()  # Levanta HTTPError se status != 200

        return r.json()

    except requests.exceptions.RequestException as e:
        print("🚨 Erro na requisição:", e)
        raise Exception(f"Erro ao acessar API Callix: {e}")

if __name__ == "__main__":
    teste = get_sub_accounts_api()
    print(teste)