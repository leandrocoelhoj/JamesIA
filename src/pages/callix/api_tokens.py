from src.core.base_page import BasePage
from src.pages.callix.xpaths import token_api, callix_page


class TokenApiPage(BasePage):
    def __init__(self, config, driver):
        """
        Create and Read Tokens.

        Args:
            config: Configuration object containing necessary settings
        """
        super().__init__(config, driver)
        self.base_url = config.get_base_url()

    def _navigate_to_api_token(self):
        """Navigate to the users page."""
        users_url = f"{self.base_url}api-tokens"
        self.driver.get(users_url)
        self.wait_for_element(callix_page['page_loaded'])

    def _create_token(self):
        self.wait_for_clickable(token_api['add_button']).click()

        self.select_option_by_text(token_api['select_token_box'], 'Administrador')
        self.find_element_and_click(token_api['save_token_button'])
        token = self.wait_for_element(token_api['token_text']).text
        return token

    def _read_tokens(self):
        elements = self.wait_and_find_elements(token_api['token_text'])

        tokens = []
        for element in elements:
            token = element.text
            tokens.append(token)
        return tokens

    def create_api_token(self):
        self._navigate_to_api_token()
        self._create_token()

    def read_tokens(self):
        self._navigate_to_api_token()
        self._read_tokens()
