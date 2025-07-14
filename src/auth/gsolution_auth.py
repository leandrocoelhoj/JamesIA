from src.core.base_auth_page import BaseAuthPage
from src.pages.gsolution.xpaths import *

class GsolutionAuthPage(BaseAuthPage):
    def login_gsolution(self):
        self.driver.get(self.config.get_base_url())
        input('teste1')
        print(self.wait_for_element(authentication['username_path']))
        input('teste1.1')
        self.wait_for_element(authentication['username_path']).send_keys('fbm.revenda')
        input('teste2')
        self.wait_for_element(authentication['password_path']).send_keys('Bill23ADM$')
        input('teste3')
        self.wait_for_element(authentication['login_button_path']).click()