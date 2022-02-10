*** Settings ***
Library  SeleniumLibrary
Resource  keywords/browser_helpers.robot
Resource  keywords/constants.robot


Suite Teardown  Close Browser
Suite Setup  Open Firefox Browser
Test Teardown  Run keyword if test failed  Fatal Error  Step failed

*** Test Cases ***
Open steam page
    Go To  ${STEAM_URL}
    Wait Until Page Contains Element  ${LOGIN_LINK_LOCATOR}
    ${current_url} =  Get Location
    Should Contain  ${current_url}  ${STEAM_URL}

Click on login link
    Click Link  ${LOGIN_LINK_LOCATOR}
    ${current_url} =  Get Location
    Wait Until Page Contains Element  ${LOGIN_BUTTON_LOCATOR}
    Should Contain  ${current_url}  ${LOGIN_URL}

Login with invalid credentials
    Input Text  ${USERNAME_FIELD_LOCATOR}  ${INVALID_USERNAME}
    Input Text  ${PASSWORD_FIELD_LOCATOR}  ${INVALID_PASSWORD}
    Click Button  ${LOGIN_BUTTON_LOCATOR}

Wait for errors
    Wait Until Element Is Visible  ${ERROR_DISPLAY_LOCATOR}
    Sleep  1 sec
    Capture Page Screenshot  invalid-credentials-attempt.png

