from src.core.base_page import BasePage
from src.pages.callix.xpaths import campaign_models, callix_page
import os
from time import sleep

class CampaignModelsPage(BasePage):
    def __init__(self, config, driver):
        """
        Initialize CampaignPage.

        Args:
            config: Configuration object containing necessary settings
        """
        super().__init__(config, driver)
        self.base_url = config.get_base_url()

    def _navigate_to_campaign_models(self):
        """Navigate to the users page."""
        users_url = f"{self.base_url}campaign-models"
        self.driver.get(users_url)
        self.wait_for_element('//*[@id="router-view"]')

    def _set_form_campaign_details(self, crm: str):
        """Set the initial details for form campaign."""
        self.wait_for_element(callix_page['page_loaded'])
        sleep(1)

        if crm == 'vanguard':
            name = 'INSS - Vanguard'
            template_name = 'Template - INSS.xlsx'
            self.wait_for_element(campaign_models['campaign_name']).send_keys(name)

        elif crm == 'finaz':
            name = 'Finaz'
            template_name = 'Template - FINAZ.xlsx'
            self.wait_for_element(campaign_models['campaign_name']).send_keys(name)
        else:
            raise ValueError("Invalid CRM type.")

        file_path = os.path.join(os.path.dirname(__file__), 'assets', template_name)
        self.wait_for_clickable(campaign_models['import_button']).click()

        if os.path.exists(file_path):
            form_select_box = self.wait_for_element(campaign_models['form_select_box'])
            form_select_box.send_keys(file_path)
        else:
            raise FileNotFoundError("Template file not found.")

        self.wait_for_clickable(campaign_models['continue_button']).click()

    def _set_text_to_form_mapping(self, crm: str):
        self.wait_for_element(callix_page['page_loaded'])
        linha = 5 if crm == "vanguard" else 2

        codigo_select_xpath = f'/html/body/ux-dialog-container/div/div/clx-dialog/create-step/clx-panel-section/dynamic-field-type-mapper/clx-data-table/div/table/tbody/tr[{linha}]/td[2]/clx-input-row/div[1]/clx-select/clx-input-group/div/div/select'
        self.select_option_by_text(codigo_select_xpath, 'Texto')

        self.wait_for_clickable(campaign_models['continue_mapping_button']).click()

    def _form_mapping(self):
        """Configure the form mappings."""
        self.select_option_by_text(campaign_models['rotulo_select'], 'nome')
        self.wait_for_clickable(campaign_models['autofill_form']).click()

        #Use this code if autofill stops
        """
        form_items = ['nome', 'cpf', 'codigo_inss',
                      'telefone1', 'telefone2', 'telefone3',
                      'telefone4', 'telefone5', 'telefone6'
                    ]

        for item in form_items:
            self.wait_for_clickable(campaign_models['form_fields']).click()
            sleep(0.5)
            self.select_option_by_text(campaign_models['select_form_item'], item)
            self.wait_for_clickable(campaign_models['confirm_form_item']).click()
            sleep(0.5)
        """

    def _configure_form_layout(self):
        self.wait_for_element(campaign_models['rotulo_select'])

        self.wait_for_clickable(campaign_models['add_line']).click()
        self.wait_for_clickable(campaign_models['add_line']).click()

        self.select_option_by_text(campaign_models['select_form_layout_one'], '3')
        self.select_option_by_text(campaign_models['select_form_layout_two'], '3')
        self.select_option_by_text(campaign_models['select_form_layout_three'], '3')


    def create_form_campaign(self, crm: str):
        """
        Create a form campaign.

        Args:
            crm (str): The CRM type ('vanguard' or 'finaz')
        """
        self._navigate_to_campaign_models()

        self.wait_for_clickable(campaign_models['new_form_button']).click()
        self.wait_for_element(callix_page['page_loaded'])

        self._set_form_campaign_details(crm)
        self._set_text_to_form_mapping(crm)
        self._configure_form_layout()
        self._form_mapping()
        self.wait_for_clickable(campaign_models['save_button']).click()
        self.wait_for_element(campaign_models['page_load'])
        sleep(0.5)