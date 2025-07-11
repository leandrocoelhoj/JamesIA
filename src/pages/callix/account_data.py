from src.core.base_page import BasePage
from src.pages.callix.xpaths import account_data, callix_page
from time import sleep


class AccountDataPage(BasePage):
    """
    Classe responsável por interagir com a página de dados da conta
    no sistema Callix, permitindo a adição de rotas de telefonia.
    """

    def __init__(self, config, driver):
        """
        Inicializa a página de dados da conta.

        Args:
            config: Objeto de configuração contendo as configurações necessárias.
        """
        super().__init__(config, driver)
        self.base_url = config.get_base_url()

    def _navigate_to_add_route(self):
        """
        Navega até a página de dados da conta para adicionar uma rota de saída.
        """
        users_url = f"{self.base_url}account-data"
        self.driver.get(users_url)
        self.wait_for_element(callix_page['page_loaded'])

    def _add_exit_route(self, route: str):
        """
        Adiciona uma rota de saída ao sistema.

        Args:
            route (str): Nome da rota a ser adicionada.
        """
        self.wait_for_clickable(account_data['route_button']).click()
        self.select_option_by_text(account_data['route_select_box'], route)
        self.wait_for_clickable(account_data['add_button']).click()

    def _read_route_text(self):
        sleep(2)
        route = self.return_select_text(account_data['route_select_box'])
        return route

    def add_route(self, route: str):
        """
        Metodo publico para adicionar uma rota de saída.

        Args:
            route (str): Nome da rota a ser adicionada.
        """
        self._navigate_to_add_route()
        self._add_exit_route(route)

    def read_route(self):
        self._navigate_to_add_route()
        route = self._read_route_text()
        return route