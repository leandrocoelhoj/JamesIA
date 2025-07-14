from src.config.settings import IpboxConfig, CallixConfig, GsolutionConfig
from src.auth.callix_auth import CallixAuthPage
from src.auth.ipbox_auth import IpboxAuthPage
from time import sleep

def authenticate_system(system: str, driver, **kwargs):
    """
    Factory method responsible for authenticating into a system (Callix or Ipbox).

    It selects the correct configuration and login page class based on the system identifier,
    performs the login using the provided WebDriver instance, and returns the configuration
    object ready to be injected into page objects.

    Args:
        system (str): The system to authenticate with. Supported values: "callix", "ipbox".
        driver: A Selenium WebDriver instance, already initialized.
        **kwargs:
            - For "callix", requires 'team_name' (str).
            - For "ipbox", requires 'site_id' (int).

    Returns:
        CallixConfig or IpboxConfig: A configuration object with credentials and base URL
        already authenticated and ready to be injected into page objects.

    Raises:
        ValueError: If the system name is not supported or required parameters are missing.
    """
    if system == "callix":
        team_name = kwargs.get("team_name")
        if not team_name:
            raise ValueError("Parameter 'team_name' is required for Callix authentication.")

        config = CallixConfig(team_name)
        auth_page = CallixAuthPage(config, driver)
        auth_page.login_callix()
        sleep(3)

        #auth_page.wait_for_element("Tela depois de logar aqui")
        return config

    elif system == "ipbox":
        site_id = kwargs.get("site_id")
        if site_id is None:
            raise ValueError("Parameter 'site_id' is required for Ipbox authentication.")

        config = IpboxConfig(site_id)
        auth_page = IpboxAuthPage(config, driver)
        auth_page.login_ipbox()
        return config

    elif system == "gsolution":

        config = GsolutionConfig()
        auth_page = config.get_base_url()


    else:
        raise ValueError(f"Unsupported system: '{system}'. Expected 'callix' or 'ipbox'.")