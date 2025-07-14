from src.core.base_page import BasePage
from selenium.webdriver.common.by import By
from xpaths import *

class GsolutionData(BasePage):
    def __init__(self, config, driver):
        super().__init__(config, driver)
        self.base_url = config.get_base_url()

    def extrair_dados_GS(self):
        try:
            # Navegação pelos menus
            self.wait_for_clickable(menu_navigation['Relatorios']).click() # Relatórios
            self.wait_for_clickable(menu_navigation['Minutagem']).click()
            self.wait_for_clickable(menu_navigation['Periodo']).click()
            self.wait_for_clickable(menu_navigation['Ontem']).click()
            self.wait_for_clickable(menu_navigation['Filtrar']).click()

            # Captura das linhas da tabela
            linhas = self.wait_and_find_elements(linhas_tabelas)

            dados = []
            for linha in linhas:
                colunas = linha.find_elements(By.TAG_NAME, "td")
                if colunas:
                    dados.append([col.text.strip() for col in colunas])

            return dados

        except Exception as e:
            print(f" Erro ao extrair dados: {e}")
            return []

    def salvar_dados_json(driver, dados_tabela, nome_arquivo="dados_gs.json"):
        try:
            campos = [
                ("Cliente", '//*[@id="site"]/table/tbody/tr/td/table/tbody/tr[2]/th[1]'),
                ("VOIP/VOIP", '//*[@id="site"]/table/tbody/tr/td/table/tbody/tr[2]/th[2]'),
                ("Minutos", '//*[@id="site"]/table/tbody/tr/td/table/tbody/tr[2]/th[3]'),
                ("Valor Venda", '//*[@id="site"]/table/tbody/tr/td/table/tbody/tr[2]/th[4]'),
                ("Custo", '//*[@id="site"]/table/tbody/tr/td/table/tbody/tr[2]/th[5]'),
                ("Lucro", '//*[@id="site"]/table/tbody/tr/td/table/tbody/tr[2]/th[6]'),
                ("Lucratividade", '//*[@id="site"]/table/tbody/tr/td/table/tbody/tr[2]/th[7]'),
                ("Rentabilidade", '//*[@id="site"]/table/tbody/tr/td/table/tbody/tr[2]/th[8]')
            ]

            cabecalhos = {campo: obter_texto(driver, xpath) for campo, xpath in campos}
            cabecalhos["Dados"] = dados_tabela

            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                json.dump(cabecalhos, f, indent=4, ensure_ascii=False)

            print(f"Dados salvos, arquivo: {nome_arquivo}")
            return True

        except Exception as e:
            print(f"Ops, teve erro ao salvar o JSON rs: {e}")
            return False