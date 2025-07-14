from src.core.base_page import BasePage
from src.pages.callix.xpaths import teams_paths, callix_page
from time import sleep


class TeamPage(BasePage):
    def __init__(self, config, driver):
        """
        Initialize TeamPage.

        Args:
            config: Configuration object containing necessary settings
        """
        super().__init__(config, driver)
        self.base_url = config.get_base_url()

    def navigate_to_teams(self):
        """Navigate to the teams page."""
        teams_url = f"{self.base_url}teams"
        self.driver.get(teams_url)
        self.wait_for_element(callix_page['page_loaded'])

    def _configure_dropdown(self):
        self.select_option_by_text(teams_paths['group_pauses_select'], 'Pausas padrão')

        manual_checkbox = self.wait_for_clickable(teams_paths['manual_call_checkbox'])
        manual_checkbox.click()

        self.wait_for_clickable(teams_paths['client_default_form'])
        self.select_option_by_text(teams_paths['client_default_form'], 'Formulário Padrão')
        self.select_option_by_text(teams_paths['cpc_select'], 'Qualificações Padrão')
        self.select_option_by_text(teams_paths['not_cpc_select'], 'Qualificações Padrão')
        self.select_option_by_text(teams_paths['supervisor_group_select'], 'Grupo de supervisão padrão')

    def _set_route(self):
        sleep(5)
        self.wait_for_clickable(teams_paths['manual_route_button']).click()
        self.select_option_by_text(teams_paths['manual_route_selection'], "#Geral - VenditoreBLF_Manual (Tech: 6014)")

    def _team_name(self, team_name):
        return self.find_element_and_send_keys(teams_paths['team_name_input'], f"{team_name.capitalize()} 01")

    def create_teams(self, team_name):
        """Create teams/groups within the system."""
        self.navigate_to_teams()
        self.wait_for_clickable(teams_paths['add_button']).click()

        self._team_name(team_name)
        self._configure_dropdown()
        self._set_route()
        self.wait_for_clickable(teams_paths['confirm_button']).click()