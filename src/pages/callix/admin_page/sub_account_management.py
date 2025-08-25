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

    def _get_all_subdomains_data_info(self):
        import logging
        domains_list = []
        sleep(1)
        try:
            logging.info("Esperando tabela de domínios aparecer na página.")
            self.wait_for_element('//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')
            domains_list.extend(self._get_subdomains_data_info())
            logging.info("Primeira página coletada com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao enviar dados na primeira página: {e}")
            raise

        page_number = 1
        while True:
            try:
                botao_avancar = self.driver.find_element(
                    By.XPATH, '//*[@id="__next"]/div/div[3]/div[2]/div/div[3]/div[2]/button[3]'
                )
                if 'disabled' in botao_avancar.get_attribute('class') or botao_avancar.get_attribute('disabled'):
                    logging.info(f"O botão está desabilitado. Fim da paginação na página {page_number}.")
                    break
                else:
                    botao_avancar.click()
                    logging.info(f"Avançando para a próxima página ({page_number + 1}).")
            except Exception as e:
                logging.error(f"Erro ao processar paginação na página {page_number}: {e}")
                break

            try:
                self.wait_for_element('//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')
                domains_list.extend(self._get_subdomains_data_info())
                logging.info(f"Página {page_number + 1} coletada com sucesso.")
                page_number += 1
            except Exception as e:
                logging.error(f"Erro ao coletar dados na página {page_number}: {e}")
                break

        logging.info(f"Paginação concluída. Total de domínios coletados: {len(domains_list)}")
        return domains_list

    def _get_subdomains_data_info(self):
        domains_list = []

        self.wait_for_element('//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')
        rows = self.driver.find_elements(By.XPATH,
                                         '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr')

        for index, row in enumerate(rows, start=1):
            try:
                team_name = row.find_element(By.XPATH, './td[1]').text

                if row.find_element(By.XPATH, './td[2]'):
                    domain = row.find_element(By.XPATH, './td[2]').text
                else:
                    domain = row.find_element(By.XPATH, './td[2]/a').text

                team_status = row.find_element(By.XPATH, './td[3]').text
                team_pas = row.find_element(By.XPATH, './td[4]').text
                team_ramais = row.find_element(By.XPATH, './td[5]').text
                team_data_entrada = row.find_element(By.XPATH, './td[7]').text

                "td[2]"

                domain_info = {
                    "equipe": team_name,
                    "dominio": domain.strip(),
                    "status": team_status,
                    "pas": team_pas,
                    "ramais": team_ramais,
                    "data-entrada": team_data_entrada
                }

                domains_list.append(domain_info)

            except Exception as e:
                msg = str(e).split('\n')[0]
                print(f"Erro ao processar a linha {index}: {msg}")
                continue

        return domains_list

    def get_domains(self):
        self.navigate_to_sub_accounts()
        self.wait_for_clickable('//*[@id="__next"]/div/div[1]/button').click()
        domains_list = self._get_all_subdomains_data_info()
        return domains_list


# if __name__ == "__main__":
#     config = authenticate_callix('contechsystem')
#
#     sub_accounts_page = SubAccountPage(config)
#
#     sub_accounts_page.navigate_to_sub_accounts()
#     sub_accounts_page._get_subdomains_data_info()
#     input('teste')