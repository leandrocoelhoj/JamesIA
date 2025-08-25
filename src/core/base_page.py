from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BasePage:
    """Base class for all pages, providing common utilities and WebDriver access."""

    def __init__(self, config, driver):
        """
        Initialize a page with configuration and WebDriver instance.

        Args:
            config: Configuration object containing URLs and credentials
        """
        self.config = config
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def wait_for_element(self, locator):
        """Wait for an element to be present and return it."""
        return WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, f"{locator}")))

    def wait_for_clickable(self, locator):
        """Wait for an element to be clickable and."""
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, f"{locator}")))

    def select_option_by_text(self, locator, text):
        """Select an option from a dropdown by visible text."""
        self.wait_for_element(locator)
        element = self.driver.find_element(By.XPATH, locator)

        #self.driver.execute_script("arguments[0].click();", element)

        select = Select(element)
        select.select_by_visible_text(text)

    def return_select_text(self, locator):
        self.wait_for_element(locator)
        element = self.driver.find_element(By.XPATH, locator)
        select = Select(element)
        selected_option  = select.first_selected_option
        text = selected_option.text
        return text

    def find_element_and_click(self, locator):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, f"{locator}"))).click()

    def find_element_and_send_keys(self, locator, keys):
        element = self.driver.find_element(By.XPATH, locator)

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        self.wait.until(EC.visibility_of(element))
        self.wait.until(EC.element_to_be_clickable(element))

        element.clear()
        element.send_keys(keys)

    def wait_and_find_elements(self, locator):
        self.wait_for_element(locator)
        elements = self.driver.find_elements(By.XPATH, locator)
        return elements

    def select_option_by_text_no_wait(self, locator, text):
        """Select an option from a dropdown by visible text."""
        element = self.driver.find_element(By.XPATH, locator)
        select = Select(element)
        select.select_by_visible_text(text)