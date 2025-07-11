import os
from dotenv import load_dotenv

load_dotenv()

"""
- Aqui são utilizadas as credenciais carregas do arquivo .env
- As autenticações são separadas por classes isoladas pra cada sistema.
- As Classes vão ser chamadas dentro de "factory.py" onde vai ter um método que vai instanciar essa classe
e chamar outra classe de autenticação que fica na estrutura de cada sistema como "login.py".

- As classes de login.py devem receber BasePage como classe pai.
"""

class CallixConfig:
    def __init__(self, team_name: str):
        """
        Inicializa a configuração para uma equipe específica.

        Args:
            team_name (str): Nome da equipe, utilizado para construir a URL.
        """
        self.team_name = team_name
        self.user = os.getenv("CALLIX_USER")
        self.password = os.getenv("CALLIX_PASSWORD1")
        self.email = os.getenv("CALLIX_EMAIL")

    def get_base_url(self) -> str:
        """
        Constrói e retorna a URL base para a equipe.

        Returns:
            str: URL no formato "https://{team_name.lower()}.callix.com.br/"
        """
        return f"https://{self.team_name.lower()}.callix.com.br/"

class IpboxConfig:
    def __init__(self, site: int):
        """
        Inicializa a configuração para uma equipe específica.

        Args:
            team_name (str): Nome da equipe, utilizado para construir a URL.
        """
        self.site = site
        self.user = os.getenv("IPBOX_USER")
        self.password = os.getenv("IPBOX1_PASSWORD")
        self.password = os.getenv("IPBOX2_PASSWORD")

    def get_base_url(self) -> int:
        """
        Constrói e retorna a URL base para a equipe.

        Returns:
            str: URL no formato "https://{team_name.lower()}.callix.com.br/"
        """

        if self.site == 1:
            return "https://contech1.ipboxcloud.com.br:8624/"
        elif self.site == 3:
            return "https://contech3.ipboxcloud.com.br:9972/"

