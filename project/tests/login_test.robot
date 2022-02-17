*** Settings ***
Documentation  Verifies error assertion with invalid login credentials
Default Tags  Smoke

Variables  configuration/constants.py
Library  framework/utils/browser_manager/BrowserManager.py
Library  project/steps/steam_login_steps.py
Library  project/steps/common_steps.py

Suite Setup  Test Setup
Suite Teardown  Test Teardown
Test Teardown  Run keyword if test failed  Fatal Error  Step failed

*** Keywords ***
Test Setup
    ${browser} =  Get Browser  ${BROWSER_TYPE}
    Set Suite Variable  ${browser}  ${browser}
    ${page_object} =  Go To Login Page  ${browser}
    Set Suite Variable  ${page_object}  ${page_object}

Test Teardown
    Close Browser  ${browser}

*** Test Cases ***


Log in With Invalid Credentials
    Login With Credentials  ${page_object}  ${INVALID_USERNAME}  ${INVALID_PASSWORD}
    Sleep  1 sec
    Capture Error Message  ${page_object}

