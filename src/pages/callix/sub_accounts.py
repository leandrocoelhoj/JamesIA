from src.core.base_page import BasePage
from src.pages.callix.xpaths import users_paths, callix_page


class SubAccount(BasePage):
    """Handles user management operations in the Callix system."""

    def __init__(self, config, driver):
        super().__init__(config, driver)
        self.base_url = config.get_base_url()

    def navigate_to_subaccount(self):
        """Navigate to the users page."""
        users_url = "https://contechsystem.callix.com.br/"
        self.driver.get(users_url)
        self.wait_for_element(callix_page["page_loaded"])

    def list_accounts(self):
        self.navigate_to_subaccount()
