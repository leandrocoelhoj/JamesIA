supervisor_profile_list = ['//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row/div[1]/clx-tree-view/ul/li[2]/ul/li[1]/div/checkbox-node/clx-check/div/label',
'//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row/div[1]/clx-tree-view/ul/li[3]/ul/li[1]/ul/li[1]/ul/li[1]/div/checkbox-node/clx-check/div/label',
'//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row/div[1]/clx-tree-view/ul/li[3]/ul/li[1]/ul/li[1]/ul/li[4]/div/checkbox-node/clx-check/div/label',
'//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row/div[1]/clx-tree-view/ul/li[3]/ul/li[1]/ul/li[2]/div/checkbox-node/clx-check/div/label',
'//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row/div[1]/clx-tree-view/ul/li[3]/ul/li[1]/ul/li[3]/div/checkbox-node/clx-check/div/label',
'//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row/div[1]/clx-tree-view/ul/li[3]/ul/li[1]/ul/li[4]/div/checkbox-node/clx-check/div/label',
'//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row/div[1]/clx-tree-view/ul/li[3]/ul/li[2]/div/checkbox-node/clx-check/div/label',
'//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row/div[1]/clx-tree-view/ul/li[5]/div/checkbox-node/clx-check/div/label',
'//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row/div[1]/clx-tree-view/ul/li[8]/ul/li[2]/ul/li[5]/div/checkbox-node/clx-check/div/label',
'//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row/div[1]/clx-tree-view/ul/li[8]/ul/li[3]/ul/li[3]/div/checkbox-node/clx-check/div/label'
]

perfil_acess_paths = {
    'add_button': '//*[@id="router-view"]/clx-page/div[1]/div/div[2]/div/a',
    'perfil_acess_name': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[1]/div[2]/div/clx-panel-section/clx-input-row[1]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'confirm_button': '//*[@id="router-view"]/clx-page/div[2]/div/div[2]/div/clx-button/button',
    'confirm_integration_selection': '/html/body/ux-dialog-container/div/div/clx-dialog/div/clx-button[1]/button'
}

integration_paths = {
    'add_integration': '/html/body/ux-dialog-container/div/div/clx-dialog/div/clx-button[1]/button',
    'add_button': '//*[@id="router-view"]/clx-page/div[1]/div/div[2]/div/clx-button/button',
    'agencia': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/compose/clx-panel[1]/div[2]/div/clx-panel-section/clx-input-row[2]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'integration_select': '/html/body/ux-dialog-container/div/div/clx-dialog/clx-input-row/div[1]/clx-select/clx-input-group/div/div/select',
    'confirm_button': '//*[@id="router-view"]/clx-page/div[2]/div/div[2]/div/clx-button/button',
    'status_select': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/compose/clx-panel[1]/div[2]/div/clx-panel-section/clx-input-row[1]/div[1]/status-toggle/clx-select/clx-input-group/div/div/select',

    'button_ramal_one': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/compose/clx-panel[3]/div[2]/div/clx-panel-section/user-extensions/clx-input-row',
    'button_ramal_two': '/div[1]/clx-button/button',
    'add_agent_one': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/compose/clx-panel[3]/div[2]/div/clx-panel-section/user-extensions/clx-input-row',
    'add_agent_two': '/div[1]/clx-select/clx-input-group/div/div/select',
    'add_ramal_one': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/compose/clx-panel[3]/div[2]/div/clx-panel-section/user-extensions/clx-input-row',
    'add_ramal_two': '/div[1]/clx-text-input/clx-input-group/div/div[2]/input',

    'ramal': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/compose/clx-panel[3]/div[2]/div/clx-panel-section/user-extensions/clx-input-row[1]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'user_ramal': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/compose/clx-panel[3]/div[2]/div/clx-panel-section/user-extensions/clx-input-row[1]/div[1]/clx-select/clx-input-group/div/div/select'
}

users_paths = {
    'add_button': '//*[@id="router-view"]/clx-page/div[1]/div/div[2]/div/a[2]',
    'user_name': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[1]/div[2]/div/clx-panel-section/clx-input-row[2]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'user_email': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[1]/div[2]/div/clx-panel-section/clx-input-row[3]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'user_login': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row[2]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'equip_select': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[3]/div[2]/div/clx-panel-section/clx-input-row[1]/div[1]/clx-select/clx-input-group/div/div/select',
    'acess_profile_select': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row[1]/div[1]/clx-select/clx-input-group/div/div/select',
    'confirm_button': '//*[@id="router-view"]/clx-page/div[2]/div/div[2]/div/clx-button/button',
    'user_qtd_select': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/clx-pagination/span[2]/clx-select/clx-input-group/div/div/select',
    'user_password_input1': '/html/body/ux-dialog-container/div/div/clx-dialog/clx-panel-section/form/clx-input-row[1]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'user_password_input2': '/html/body/ux-dialog-container/div/div/clx-dialog/clx-panel-section/form/clx-input-row[2]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'save_password_button': '/html/body/ux-dialog-container/div/div/clx-dialog/clx-panel-section/form/div/button',
    'settings_button': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/div/table/tbody/tr/td[8]/clx-button/button',
    'delete_option_from_setting': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/div/table/tbody/tr/td[9]/clx-button/ul/li[4]',
    'confirm_delete': '/html/body/ux-dialog-container/div/div/clx-dialog/div/clx-button[2]/button',
    'search_input': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/clx-filter/div/div/clx-text-input/clx-input-group/div/div[2]/input',
    'search_button': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/clx-filter/div/div/clx-button[1]/button',
    'user_row_base': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/div/table/tbody/tr',
    'user_row_base_full': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/div/table/tbody/tr/td[9]/clx-button/button',
    'change_password_option_one': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/div/table/tbody/tr',
    'change_password_option_two': '/td[9]/clx-button/ul/li[2]'
}

authentication = {
    'username_path': '/html/body/div/router-view/div/clx-input-row[1]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'teste': '/html/body/div/router-view/div/clx-input-row[1]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'password_path': '/html/body/div/router-view/div/clx-input-row[2]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'login_button_path': '/html/body/div/router-view/div/button'
}

teams_paths = {
    'add_button': '//*[@id="router-view"]/clx-page/div[1]/div/div[2]/div/a',
    'confirm_button': '//*[@id="router-view"]/clx-page/div[2]/div/div[2]/div/clx-button/button',
    'team_name_input': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[1]/div[2]/div/clx-panel-section/clx-input-row[1]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'group_pauses_select': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[1]/div[2]/div/clx-panel-section/clx-input-row[3]/div[1]/clx-select/clx-input-group/div/div/select',
    'manual_call_checkbox': "//label[contains(normalize-space(.), 'Permitir discagem manual')]",
    'client_default_form': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[7]/div[2]/div/clx-panel-section/clx-input-row[1]/div[1]/clx-select/clx-input-group/div/div/select',
    'cpc_select': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[7]/div[2]/div/clx-panel-section/clx-input-row[7]/div[1]/clx-select/clx-input-group/div/div/select',
    'not_cpc_select': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[7]/div[2]/div/clx-panel-section/clx-input-row[8]/div[1]/clx-select/clx-input-group/div/div/select',
    'supervisor_group_select': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[7]/div[2]/div/clx-panel-section/clx-panel-section/clx-input-row/div[1]/clx-select/clx-input-group/div/div/select',
    'manual_route_button': "//label[contains(normalize-space(.), 'Rota própria')]",
    'manual_route_selection': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[6]/div[2]/div/clx-panel-section/div[2]/clx-panel-section[6]/route-configuration/div/div[1]/div/div/clx-input-row/div[1]/clx-select/clx-input-group/div/div/select'
}


campaigns = {
    'name': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row[1]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    #'del_description': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row[2]/div[1]/clx-text-input/clx-input-group/div/div[2]/button',
    'del_cx_postal': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[4]/div[2]/div/dialing-configuration-form/clx-panel-section[1]/clx-input-row[5]/div[1]/clx-check/div/label',
    #'del_advanced_config': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[4]/div[2]/div/dialing-configuration-form/clx-panel-section[1]/clx-input-row[5]/div[1]/clx-check/div/label',
    'change_agress': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[5]/div[2]/div/campaign-type-form/clx-panel-section/div[2]/clx-input-row/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'select_equip': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[8]/div[2]/div/campaign-user-form/clx-panel-section[1]/clx-input-row[2]/div[1]/clx-select/clx-input-group/div/div/select',
    'select_cpc': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[8]/div[2]/div/campaign-user-form/clx-panel-section[2]/clx-input-row[6]/div[1]/clx-select/clx-input-group/div/div/select',
    'select_not_cpc': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[8]/div[2]/div/campaign-user-form/clx-panel-section[2]/clx-input-row[7]/div[1]/clx-select/clx-input-group/div/div/select',
    'supervisor_group': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[8]/div[2]/div/campaign-user-form/clx-panel-section[3]/clx-input-row/div[1]/clx-select/clx-input-group/div/div/select',
    'save_button': '//*[@id="router-view"]/clx-page/div[2]/div/div[2]/div/clx-button/button'
}

token_api = {
    'token_text': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/div/table/tbody/tr/td[1]/a',
    'add_button': '//*[@id="router-view"]/clx-page/div[1]/div/div[2]/div/button',
    'select_token_box': '/html/body/ux-dialog-container/div/div/clx-dialog/clx-panel-section/form/clx-input-row/div[1]/clx-select/clx-input-group/div/div/select',
    'save_token_button': '/html/body/ux-dialog-container/div/div/clx-dialog/clx-panel-section/form/div/button',
    'copy_token': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/div/table/tbody/tr/td[1]/a'
}

account_data = {
    'route_button': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[5]/div[2]/div/clx-panel-section/route-configuration/div/div[1]/div/clx-input-row[1]/div[1]/clx-check-group/clx-input-group/div/div/div/clx-check[2]/div/label',
    'route_select_box': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[5]/div[2]/div/clx-panel-section/route-configuration/div/div[1]/div/div/clx-input-row/div[1]/clx-select/clx-input-group/div/div/select',
    'add_button': '//*[@id="router-view"]/clx-page/div[2]/div/div[2]/div/clx-button/button'
}

campaign_paths = {
    # For scrap
    'campaign_link': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/div/table/tbody/tr/td[3]/a[2]',
    'maxtries_input': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[4]/div[2]/div/dialing-configuration-form/clx-panel-section[1]/clx-input-row[1]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',

    #For configuration
    'add_campaign_button': '//*[@id="router-view"]/clx-page/div[1]/div/div[2]/div/clx-button[1]/button',
    'new_campaign_option': '//*[@id="router-view"]/clx-page/div[1]/div/div[2]/div/clx-button[1]/ul/li[1]/a',
    'campaign_name':'//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section/clx-input-row[1]/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'form_select': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[3]/div[2]/div/clx-panel-section/clx-input-row[2]/div[1]/clx-select/clx-input-group/div/div/select',
    'dialing_checkbox': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[4]/div[2]/div/dialing-configuration-form/clx-panel-section[1]/clx-input-row[5]/div[1]/clx-check/div/label',
    'campaign_type_checkbox': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[5]/div[2]/div/campaign-type-form/clx-panel-section/clx-input-row/div[1]/clx-check-group/clx-input-group/div/div/div/clx-check[2]/div/label',
    'attempts_input': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[5]/div[2]/div/campaign-type-form/clx-panel-section/div[2]/clx-input-row/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'select_equip': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[8]/div[2]/div/campaign-user-form/clx-panel-section[1]/clx-input-row[2]/div[1]/clx-select/clx-input-group/div/div/select',
    'select_cpc': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[8]/div[2]/div/campaign-user-form/clx-panel-section[2]/clx-input-row[6]/div[1]/clx-select/clx-input-group/div/div/select',
    'select_not_cpc': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[8]/div[2]/div/campaign-user-form/clx-panel-section[2]/clx-input-row[7]/div[1]/clx-select/clx-input-group/div/div/select',
    'supervisor_group': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[8]/div[2]/div/campaign-user-form/clx-panel-section[3]/clx-input-row/div[1]/clx-select/clx-input-group/div/div/select',
    'select_team': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[8]/div[2]/div/campaign-user-form/clx-panel-section[1]/clx-input-row[2]/div[1]/clx-select/clx-input-group/div/div/select',


    'post-sale': ['//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[8]/div[2]/div/campaign-user-form/clx-panel-section[2]/clx-input-row[3]/div[1]/clx-duration-input/clx-input-group/div/div/div/input[1]',
                  '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[8]/div[2]/div/campaign-user-form/clx-panel-section[2]/clx-input-row[3]/div[1]/clx-duration-input/clx-input-group/div/div/div/input[2]',
                  '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[8]/div[2]/div/campaign-user-form/clx-panel-section[2]/clx-input-row[3]/div[1]/clx-duration-input/clx-input-group/div/div/div/input[3]'
                ],
    'save_button': '//*[@id="router-view"]/clx-page/div[2]/div/div[2]/div/clx-button/button',
    'page_load': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/div/table/tbody/tr/td[3]'
}

campaign_models = {
    'campaign_name': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[1]/div[2]/div/clx-panel-section/clx-input-row/div[1]/clx-text-input/clx-input-group/div/div[2]/input',
    'new_form_button': '//*[@id="router-view"]/clx-page/div[1]/div/div[2]/div/a',
    'import_button': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section[4]/clx-input-row/div[1]/clx-alert/div[2]/div[2]/clx-button[2]/button',
    'form_select_box': '/html/body/ux-dialog-container/div/div/clx-dialog/import-step/clx-panel-section/clx-input-row/div[1]/clx-filepicker/clx-input-group/div/div/div/input',
    'continue_button': '/html/body/ux-dialog-container/div/div/clx-dialog/import-step/div/clx-button[2]/button',
    'continue_mapping_button': '/html/body/ux-dialog-container/div/div/clx-dialog/create-step/clx-panel-section/div[2]/clx-button[3]/button',
    'rotulo_select': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[2]/div[2]/div/clx-panel-section[5]/clx-input-row/div[1]/clx-select/clx-input-group/div/div/select',
    'add_line': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[3]/div[2]/div/clx-panel-section/clx-input-row[2]/div[1]/clx-form-builder/div[2]/clx-button/button',
    'select_form_layout_one': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[3]/div[2]/div/clx-panel-section/clx-input-row[2]/div[1]/clx-form-builder/div[1]/form-builder-row[1]/div[1]/clx-select/clx-input-group/div/div/select',
    'select_form_layout_two': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[3]/div[2]/div/clx-panel-section/clx-input-row[2]/div[1]/clx-form-builder/div[1]/form-builder-row[2]/div[1]/clx-select/clx-input-group/div/div/select',
    'select_form_layout_three': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[3]/div[2]/div/clx-panel-section/clx-input-row[2]/div[1]/clx-form-builder/div[1]/form-builder-row[3]/div[1]/clx-select/clx-input-group/div/div/select',
    'form_fields': '((//*[@id="null"]/form-builder-field/div)[1])',
    'select_form_item': '/html/body/ux-dialog-container/div/div/clx-dialog/clx-input-row/div[1]/clx-select/clx-input-group/div/div/select',
    'confirm_form_item': '/html/body/ux-dialog-container/div/div/clx-dialog/div/clx-button[1]/button',
    'save_button': '//*[@id="router-view"]/clx-page/div[2]/div/div[2]/div/clx-button/button',
    'autofill_form': '//*[@id="router-view"]/clx-page/div[2]/div/div[1]/div[2]/clx-panel[3]/div[2]/div/clx-panel-section/clx-input-row[1]/div[1]/clx-button/button',
    'page_load': '//*[@id="router-view"]/clx-page/div[2]/clx-data-table/div/table/tbody/tr/td[1]'
}

callix_page = {'page_loaded': '//*[@id="router-view"]'}


sub_accounts = {
    'subdomain_link': '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/a',
    'next_page_button': '//*[@id="__next"]/div/div[3]/div[2]/div/div[3]/div[2]/button[3]',
    'domain_line': '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr',
    'domain_name': '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]',
    'domain_link': '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr/td[2]/a',
    'domain_status': '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr/td[3]',
    'domain_pas': '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr/td[4]',
    'domain_ramais': '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr/td[5]',
    'domain_data_entrada': '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr/td[7]'
}