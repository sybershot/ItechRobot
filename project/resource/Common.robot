*** Settings ***
Variables  project/configuration/constants.py
Variables  itechframework/configuration/config.py
Library  itechframework.modules.browser_manager.BrowManRobot
Library  project.steps.CommonSteps


*** Keywords ***
Open Browser
    ${browser} =  Get Browser  ${BROWSER_TYPE}
    Set Suite Variable  ${browser}

Close Browser
    Destroy Browser  ${browser}