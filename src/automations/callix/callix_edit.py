from src.pages.callix.users import UserPage
from src.auth.factory import authenticate_system
from src.pages.callix.admin_page.sub_account_management import SubAccountPage
from time import sleep
from selenium import webdriver

def domains():
    team_name = 'contechsystem'
    driver = webdriver.Chrome()
    config = authenticate_system(system='callix', team_name=team_name, driver=driver)
    sub_accounts_page = SubAccountPage(config, driver)
    domains_list = sub_accounts_page.get_domains()
    return domains_list

def create_single_user(users_name):
    domains_list = domains()
    driver = webdriver.Chrome()
    for domain in domains_list:
        domain_name = domain.get("domain_link")

        try:
            config2 = authenticate_system(system='callix', team_name=domain_name, driver=driver)
            user_page = UserPage(config2, driver)
            for user in users_name:
                user_page.create_adm_user()
                user_page.update_all_passwords(user, 0)
                sleep(0.5)

        except:
            print(f'Não foi possível acessar o ambiente: {domain_name}')
            continue

if __name__ == '__main__':
    create_single_user(['Victor'])





