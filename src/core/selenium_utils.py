import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_driver():
    """
    Configura e retorna uma instância do WebDriver do Chrome com opções otimizadas para Docker/headless.
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    tmp_profile = tempfile.TemporaryDirectory()
    options.add_argument(f'--user-data-dir={tmp_profile.name}')

    driver = webdriver.Chrome(options=options)
    # GUARDE tmp_profile JUNTO do driver para não ser limpo antes da hora!
    driver._tmp_profile = tmp_profile  # Hack: adiciona como atributo do driver
    return driver