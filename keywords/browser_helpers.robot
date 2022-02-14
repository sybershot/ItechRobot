*** Settings ***
Library  framework/utils/drivermanager/driver_manager.py



*** Keywords ***
Open Browser
    [Arguments]  ${browser_type}=Firefox
    ${browser} =  get_browser  ${browser_type}
    [Return]  ${browser}
