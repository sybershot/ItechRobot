*** Settings ***
Variables  configuration/constants.py

*** Keywords ***
Test Setup
    ${browser} =  Get Browser  ${BROWSER_TYPE}
    Set Suite Variable  ${browser}  ${browser}
    ${page_object} =  Go To Steam Page  ${browser}
    Set Suite Variable  ${page_object}  ${page_object}

Test Teardown
    Close Browser  ${browser}