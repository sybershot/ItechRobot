*** Settings ***
Documentation  Verifies ability to download steam client app
Default Tags  Smoke

Variables  configuration/constants.py
Library  framework/utils/browser_manager/BrowserManager.py
Library  project/steps/CommonSteps.py
Library  project/steps/SteamDownloadSteps.py
Resource  project/resource.robot

Suite Setup  Test Setup
Suite Teardown  Test Teardown
Test Teardown  Run keyword if test failed  Fatal Error  Step Failed

*** Test Cases ***

Download Steam Client
    ${page_object} =  Go To Download Page  ${page_object}
    Click Download Button  ${page_object}