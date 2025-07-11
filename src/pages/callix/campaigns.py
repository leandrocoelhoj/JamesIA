from time import sleep

from src.core.base_page import BasePage
from src.pages.callix.xpaths import campaign_paths, callix_page


class CampaignPage(BasePage):
    def __init__(self, config, driver):
        """
        Initialize CampaignPage.

        Args:
            config: Configuration object containing necessary settings
        """
        super().__init__(config, driver)
        self.base_url = config.get_base_url()

    def navigate_to_campaign(self):
        """Navigate to the users page."""
        users_url = f"{self.base_url}campaigns"
        self.driver.get(users_url)
        self.wait_for_element(callix_page['page_loaded'])

    def create_campaign(self, crm: str, team_name: str):
        """
        Create a new campaign.

        Args:
            crm (str): The CRM type ('vanguard' or 'finaz')
            :param crm:
            :param team_name:
        """
        self.navigate_to_campaign()

        #self._configure_phone_max_tries(1)

        self.wait_for_clickable(campaign_paths['add_campaign_button']).click()
        self.wait_for_clickable(campaign_paths['new_campaign_option']).click()

        self.wait_for_element(campaign_paths['save_button'])

        self.wait_for_element(campaign_paths['campaign_name'])
        self.find_element_and_send_keys(campaign_paths['campaign_name'],'INSS')

        #Código está buscando por string com INSS - Vanguard e quando não existe a string está levantando erro.
        self.select_option_by_text(
            campaign_paths['form_select'],
            'INSS - Vanguard' if crm == "vanguard" else 'Finaz'
        )

        self._configure_campaign_agress('4')
        self._configure_campaign_post_sale()
        self._configure_campaign_max_tries('1')
        self._configure_dropdowns(team_name)

        self.wait_for_clickable(campaign_paths['save_button']).click()
        self.wait_for_element(campaign_paths['page_load'])
        sleep(0.5)

    def _configure_dropdowns(self, team_name):
        """Configure all dropdown selections for the campaign."""
        dropdown_configs = [
            (campaign_paths['select_equip'], 'Administração'),
            (campaign_paths['select_cpc'], 'Qualificações Padrão'),
            (campaign_paths['select_not_cpc'], 'Qualificações Padrão'),
            (campaign_paths['supervisor_group'], 'Grupo de supervisão padrão'),
            (campaign_paths['select_team'], f'{team_name.capitalize()} 01')
        ]

        for xpath, value in dropdown_configs:
            self.select_option_by_text(xpath, value)

    def _configure_campaign_agress(self, agress):
        """Configure campaign agress"""
        try:
            self.wait_for_clickable(campaign_paths['dialing_checkbox']).click()
            self.wait_for_clickable(campaign_paths['campaign_type_checkbox']).click()
        except:
            print('Não foi possível clicar no "Power"')
            pass

        attempts_field = self.wait_for_element(campaign_paths['attempts_input'])
        attempts_field.clear()
        attempts_field.send_keys(agress)

    def _configure_campaign_max_tries(self, tries: str):
        """Configure campaign agress"""
        self.wait_for_clickable(campaign_paths['maxtries_input'])
        self.driver.find_element('xpath', campaign_paths['maxtries_input']).clear()
        self.driver.find_element('xpath', campaign_paths['maxtries_input']).send_keys(tries)

    def _configure_campaign_post_sale(self):
        """Configure campaign post sale"""
        #Futuramente implementar f string no script pra que possamos setar o pós atendimento que quisermos e rodar.
        horas_input = self.driver.find_element('xpath', campaign_paths['post-sale'][0])
        minutos_input = self.driver.find_element('xpath', campaign_paths['post-sale'][1])
        segundos_input = self.driver.find_element('xpath', campaign_paths['post-sale'][2])

        self.driver.execute_script("arguments[0].value = '0';", horas_input)
        self.driver.execute_script("arguments[0].value = '0';", minutos_input)
        self.driver.execute_script("arguments[0].value = '10';", segundos_input)

    def _edit_campaign(self, qtd, agress):
        self.navigate_to_campaign()


    def _scrap_campaign_quantity(self):
        self.navigate_to_campaign()
        links = []

        campaign_links = self.wait_and_find_elements(campaign_paths['campaign_link'])
        for campaign in campaign_links:
            campaign_link = campaign.get_attribute('href')
            links.append(campaign_link)
        return links

    def _access_campaign(self, campaign_link):
        self.driver.get(campaign_link)
        self.wait_for_element(callix_page['page_loaded'])