*** Settings ***
Documentation  This test verifies error assertion when user logs in with incorrect credentials
Default Tags  Smoke

Variables  configuration/constants.py
Library  framework/utils/robotbrowser/RobotBrowser.py  ${BROWSER_TYPE}
Library  project/steps/steam_login_steps.py


Suite Teardown  Close Browser
Test Teardown  Run keyword if test failed  Fatal Error  Step failed

*** Test Cases ***
Test Setup
    ${browser} =  Get Browser
    ${page_object} =  Open Steam Main Page  ${browser}
    Set Suite Variable  ${page_object}  ${page_object}
