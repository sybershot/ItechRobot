*** Settings ***
Variables  project/configuration/constants.py
Variables  itechframework/configuration/config.py
Library  project.steps.CommonSteps


*** Keywords ***
Open Browser
    ${browser} =  Get Browser  ${BROWSER_TYPE}
    Set Suite Variable  ${browser}

Close Browser
    Destroy Browser  ${browser}