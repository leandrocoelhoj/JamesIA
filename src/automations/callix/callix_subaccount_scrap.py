from src.auth.factory import authenticate_system
from src.pages.callix.admin_page.sub_account_management import SubAccountPage
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.core.selenium_utils import get_chrome_driver

def rodar_teste():
    team_name = 'contechsystem'

    driver = get_chrome_driver()
    config = authenticate_system(system='callix', driver=driver, team_name=team_name)

    sub_accounts_page = SubAccountPage(config, driver)

    sub_accounts_page.navigate_to_sub_accounts()
    domains = sub_accounts_page.get_all_subdomains_data_info()
    return domains

def enviar_dados_api():
    domains = rodar_teste()
    print("DOMAINS:", domains)

    url = 'http://host.docker.internal:8000/api/enviar-dados/'
    try:
        r = requests.post(url, json=domains)
        print("STATUS:", r.status_code)
        print("RESPONSE:", r.text)
        return r.status_code
    except requests.exceptions.RequestException as e:
        print("Erro ao enviar dados:", e)
        raise

if __name__ == "__main__":
    enviar_dados_api()

