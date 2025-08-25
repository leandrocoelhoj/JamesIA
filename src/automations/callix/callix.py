from src.auth.factory import authenticate_system
from selenium import webdriver
from src.pages.callix.access_profiles import AccessProfilesPage
from src.pages.callix.account_data import AccountDataPage
from src.pages.callix.api_tokens import TokenApiPage
from src.pages.callix.campaign_models import CampaignModelsPage
from src.pages.callix.campaigns import CampaignPage
from src.pages.callix.integrations import AddIntegrations
from src.pages.callix.teams import TeamPage
from src.pages.callix.users import UserPage

#from src.pages.callix.sub_accounts import SubAccountsPage
#from src.pages.callix.supervision_groups import

def run_callix_automation_route(url, users_name, qtd, crm: str, route):
    """
    Metodo responsável por configurar novos ambientes

    :param url:
    :param users_name:
    :param qtd:
    :param crm:
    :param route:
    :return: json usuários
    """
    driver = webdriver.Chrome()
    input()
    config = authenticate_system("callix", driver, team_name=url)
    #config = authenticate_callix(driver, url)

    access_profiles = AccessProfilesPage(config, driver)
    account_data = AccountDataPage(config, driver)
    campaign_models = CampaignModelsPage(config, driver)
    campaigns_page = CampaignPage(config, driver)
    teams_page = TeamPage(config, driver)
    users_page = UserPage(config, driver)
    integration = AddIntegrations(config, driver)
    api_tokens = TokenApiPage(config, driver)

    #access_profiles.create_access_profiles()
    teams_page.create_teams(url)
    #users_page.create_adm_user()
    users = users_page.create_users(user_name=users_name, qtd=qtd)
    users_page.update_all_passwords(user_name=users_name, qtd=qtd)
    integration.run_ramal(crm=crm, agencia=34732, users=users)
    campaign_models.create_form_campaign(crm=crm)
    campaigns_page.create_campaign(crm=crm, team_name=url)
    api_tokens.create_api_token()
    #account_data.add_route(route)
    input('Finalizado')


if __name__ == "__main__":
   run_callix_automation_route(url='renovarcontech', users_name='renovar', qtd=10, crm='vanguard', route='#Geral - VenditoreBLM (Tech: 5006)')