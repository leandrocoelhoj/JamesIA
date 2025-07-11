from src.core.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SubAccountPage(BasePage):
    def __init__(self, config, driver):
        """
        Initialize SubAccountPage.

        Args:
            config: Configuration object containing necessary settings
        """
        super().__init__(config, driver)
        self.base_url = config.get_base_url()

    def navigate_to_sub_accounts(self):
        """Navigate to the subaccount page."""
        users_url = f"{self.base_url}sub-account-management/sub-accounts?pagination=0%2C100&status=3%2C2"
        self.driver.get(users_url)
        #self.wait_for_element(callix_page['page_loaded'])

    def get_all_subdomains_data_info(self):
        domains_list = []
        sleep(1)
        try:
            self.wait_for_element('//*[@id="__next"]/div/div[1]/button')
            self.wait_for_element('//*[@id="__next"]/div/div[1]/button').click()
            self.wait_for_element('//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')
            domains_list.extend(self._get_subdomains_data_info())
        except Exception as e:
            print("Erro ao enviar dados:", e)
            raise

        while True:
            try:
                botao_avancar = self.driver.find_element(By.XPATH,
                                                         '//*[@id="__next"]/div/div[3]/div[2]/div/div[3]/div[2]/button[3]')

                # Verifica se o botão está habilitado
                if 'disabled' in botao_avancar.get_attribute('class') or botao_avancar.get_attribute('disabled'):
                    print("O botão está desabilitado. Fim da paginação.")
                    break

                botao_avancar.click()

                # Espera o carregamento da próxima página
                self.wait_for_element('//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')

                # Coleta os dados da nova página e adiciona na lista
                domains_list.extend(self._get_subdomains_data_info())

            except Exception as e:
                print("Erro ao processar paginação:", e)
                break

        return domains_list

    def _get_subdomains_data_info(self):
        domains_list = []

        self.wait_for_element('//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')
        rows = self.driver.find_elements(By.XPATH,
                                         '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr')

        for index, row in enumerate(rows, start=1):
            try:
                domain_name = row.find_element(By.XPATH, './td[1]').text
                domain_link = row.find_element(By.XPATH, './td[2]/a').text
                domain_status = row.find_element(By.XPATH, './td[3]').text
                domain_pas = row.find_element(By.XPATH, './td[4]').text
                domain_ramais = row.find_element(By.XPATH, './td[5]').text
                domain_data_entrada = row.find_element(By.XPATH, './td[7]').text

                domain_info = {
                    "domain": domain_name,
                    "domain_link": domain_link.strip(),
                    "status": domain_status,
                    "pas": domain_pas,
                    "ramais": domain_ramais,
                    "data-entrada": domain_data_entrada
                }

                domains_list.append(domain_info)

            except Exception as e:
                print(f"Erro ao processar a linha {index}: {e}")
                continue

        return domains_list

    def get_domains(self):
        self.navigate_to_sub_accounts()
        domains_list = self._get_subdomains_data_info()
        return domains_list


# if __name__ == "__main__":
#     config = authenticate_callix('contechsystem')
#
#     sub_accounts_page = SubAccountPage(config)
#
#     sub_accounts_page.navigate_to_sub_accounts()
#     sub_accounts_page._get_subdomains_data_info()
#     input('teste')