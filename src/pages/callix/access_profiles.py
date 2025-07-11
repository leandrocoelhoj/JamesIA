from src.core.base_page import BasePage
from src.pages.callix.xpaths import supervisor_profile_list, perfil_acess_paths, callix_page
from time import sleep

class AccessProfilesPage(BasePage):
    def __init__(self, config, drive):
        """
        Create Access Profiles.

        Args:
            config: Configuration object containing necessary settings
        """
        super().__init__(config, drive)
        self.base_url = config.get_base_url()

    def navigate_to_access_profiles(self):
        """Navigate to the users page."""
        users_url = f"{self.base_url}access-profiles"
        self.driver.get(users_url)
        self.wait_for_element(callix_page['page_loaded'])

    def _create_administrator_profile(self):
        self.wait_for_clickable(perfil_acess_paths['add_button']).click()

        self.wait_for_element(perfil_acess_paths['perfil_acess_name'])
        self.find_element_and_send_keys(perfil_acess_paths['perfil_acess_name'], 'Administrador')

        i = 1
        while i < 11:
            self.find_element_and_click(
                f'//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div['
                f'2]/div/clx-panel-section/clx-input-row/div[1]/clx-tree-view/ul/li['
                f'{i}]/div/checkbox-node/clx-check/div/label'
            )
            i += 1

        self.find_element_and_click(perfil_acess_paths['confirm_button'])
        sleep(1)

    def _create_supervisor_profile(self):
        self.wait_for_clickable(perfil_acess_paths['add_button']).click()

        self.wait_for_element(perfil_acess_paths['perfil_acess_name'])
        self.find_element_and_send_keys(perfil_acess_paths['perfil_acess_name'], 'Supervisor')

        for xpath in supervisor_profile_list:
            self.find_element_and_click(xpath)
        self.find_element_and_click(perfil_acess_paths['confirm_button'])
        sleep(1)

    def create_access_profiles(self):
        self.navigate_to_access_profiles()
        self._create_administrator_profile()
        self._create_supervisor_profile()

