from sys import flags
from time import sleep
from src.core.base_page import BasePage
from src.pages.callix.xpaths import callix_page, integration_paths


class AddIntegrations(BasePage):
    """
            Create Integrations.
            Args:
                config: Configuration object containing necessary settings
            """
    def __init__(self, config, driver):
        super().__init__(config, driver)
        self.base_url = config.get_base_url()

    def navigate_to_integrations(self):
        """Navigate to the users page."""
        users_url = f"{self.base_url}integrations"
        self.driver.get(users_url)
        self.wait_for_element(callix_page['page_loaded'])

    def _integration_data(self, agencia: int):
        self.select_option_by_text(integration_paths['status_select'], 'Ativada')
        self.find_element_and_send_keys(integration_paths['agencia'], agencia)
        #self.wait_for_element(integration_paths['confirm_button']).click() OUTRO BUG

    def _set_ramal(self, users):
        self.wait_for_element(callix_page['page_loaded'])

        ramal = 1001
        row = 1

        if len(users) == 1:
            self.wait_for_clickable(integration_paths['button_ramal_one'] + integration_paths['button_ramal_two']).click()
            self.select_option_by_text(integration_paths['add_agent_one'] + integration_paths['add_agent_two'], users[0])
            self.find_element_and_send_keys(integration_paths['add_ramal_one'] + integration_paths['add_ramal_two'], ramal)
            self.wait_for_clickable(integration_paths['add_button']).click()

        else:
            for user in users[1:]:
                add_ramal_button = integration_paths['button_ramal_one'] + f'[{row}]' + integration_paths['button_ramal_two']
                add_agent = integration_paths['add_agent_one'] + f'[{row}]' + integration_paths['add_agent_two']
                add_ramal = integration_paths['add_ramal_one'] + f'[{row}]' + integration_paths['add_ramal_two']
                self.wait_for_clickable(add_ramal_button).click()
                self.select_option_by_text(add_agent, user)
                self.find_element_and_send_keys(add_ramal, ramal)
                ramal += 1
                row += 1

        self.wait_for_clickable(integration_paths['confirm_button']).click()

    def _create_integrations(self, crm: str, agencia: int, users: list):
        crm.lower()

        if crm == 'finaz':
            self.wait_for_clickable(integration_paths['add_button']).click()
            sleep(1)
            self.select_option_by_text(integration_paths['integration_select'], 'Finaz')
            self.find_element_and_click(integration_paths['add_integration'])
            self._integration_data(agencia)
            self._set_ramal(users)
            sleep(1)

        elif crm == 'vanguard':
            vanguard_integrations = ['Vanguard - Maximize - Siape', 'Vanguard - Maximize - INSS']
            for integration in vanguard_integrations:
                self.wait_for_clickable(integration_paths['add_button']).click()
                sleep(1)
                self.select_option_by_text(integration_paths['integration_select'], integration)
                self.find_element_and_click(integration_paths['add_integration'])
                self._integration_data(agencia)
                self._set_ramal(users)
                sleep(1)

    def run_ramal(self, crm, agencia, users):
        self.navigate_to_integrations()
        self._create_integrations(crm, agencia, users)