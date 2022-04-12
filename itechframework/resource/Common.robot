*** Settings ***
Variables  configuration/constants.py
Variables  itechframework/configuration/constants.py
Library  itechframework.resource.BrowMan
Library  project.steps.CommonSteps


*** Keywords ***
Open Browser
    ${browser} =  Get Browser  ${BROWSER_TYPE}
    Set Suite Variable  ${browser}

Close Browser
    Destroy Browser  ${browser}