from src.core.base_auth_page import BaseAuthPage
from src.pages.gsolution.xpaths import *

class CallixAuthPage(BaseAuthPage):
    def login_gsolution(self):
        self.driver.get(self.config.get_base_url())
        self.wait_for_element(authentication['username_path']).send_keys(self.user)
        self.wait_for_element(authentication['password_path']).send_keys(self.password)
        self.wait_for_element(authentication['login_button_path']).click()