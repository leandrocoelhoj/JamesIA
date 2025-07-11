from src.core.base_auth_page import BaseAuthPage
from src.pages.ipbox.xpaths import *


class IpboxAuthPage(BaseAuthPage):
    def login_ipbox(self):
        login_url = "https://contech{n}.ipboxcloud.com.br:{port}/contech/autenticacao.php".format(
            n=self.config.site,
            port="8624" if self.config.site == 1 else "9972"
        )
        self.driver.get(login_url)
        self.wait_for_element(authentication['username_path']).send_keys(self.user)
        self.wait_for_element(authentication['password_path']).send_keys(self.password)
        self.wait_for_element(authentication['login_button_path']).click()