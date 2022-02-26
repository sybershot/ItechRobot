*** Settings ***
Documentation  Verifies error assertion with invalid login credentials
Default Tags  Smoke

Variables  configuration/constants.py
Library  framework/utils/browser_manager/BrowserManager.py
Library  project/steps/SteamLoginSteps.py
Library  project/steps/CommonSteps.py
Resource  project/resource.robot

Suite Setup  Test Setup
Suite Teardown  Test Teardown
Test Teardown  Run keyword if test failed  Fatal Error  Step failed

*** Test Cases ***

Log In With Invalid Credentials
    ${invalid_username}  ${invalid_password}  Load From JSON File  Invalid
    ${page_object} =  Go To Login Page  ${page_object}
    Login With Credentials  ${page_object}  ${invalid_username}  ${invalid_password}
    Wait Until Error Visible  ${page_object}
    Capture Error Message  ${page_object}

