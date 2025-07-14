from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_driver():
    """
    Configura e retorna uma instância do WebDriver do Chrome com opções otimizadas para Docker/headless.
    """
    # options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome()