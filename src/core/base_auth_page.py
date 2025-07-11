from src.core.base_page import BasePage

class BaseAuthPage(BasePage):
    def __init__(self, config, driver):
        super().__init__(config, driver)
        self.user = config.user
        self.password = config.password
    def login(self):
        raise NotImplementedError()