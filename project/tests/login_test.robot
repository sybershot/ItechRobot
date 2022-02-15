*** Settings ***
Variables  configuration/constants.py
Library  framework/utils/drivermanager/RobotBrowser.py  ${BROWSER_TYPE}


Suite Teardown  Close Browser
Test Teardown  Run keyword if test failed  Fatal Error  Step failed

*** Test Cases ***

Open steam page
    [Documentation]  This test verifies error assertion when user logs in with incorrect credentials
    [Tags]  Sanity
    Go To  ${STEAM_URL}
    Wait until element  xpath  ${LOGIN_LINK_LOCATOR}
    ${current_url} =  Get Location
    Should Contain  ${current_url}  ${STEAM_URL}

Click on login link
    Click Element  xpath  ${LOGIN_LINK_LOCATOR}
    ${current_url} =  Get Location
    Wait Until Element  xpath  ${LOGIN_BUTTON_LOCATOR}
    Should Contain  ${current_url}  ${LOGIN_URL}

Login with invalid credentials
    Input Text  xpath  ${USERNAME_FIELD_LOCATOR}  ${INVALID_USERNAME}
    Input Text  xpath  ${PASSWORD_FIELD_LOCATOR}  ${INVALID_PASSWORD}
    Click Element  xpath  ${LOGIN_BUTTON_LOCATOR}

Wait for errors
    Wait Until Visible  xpath  ${ERROR_DISPLAY_LOCATOR}
    Sleep  1 sec
    Capture Page Screenshot  invalid-credentials-attempt.png

