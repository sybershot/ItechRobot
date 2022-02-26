*** Settings ***
Documentation  Verifies ability to use store module
Default Tags  Smoke

Variables  configuration/constants.py
Library  framework/utils/browser_manager/BrowserManager.py
Library  project/steps/CommonSteps.py
Library  project/steps/SteamStoreSteps.py
Resource  project/resource.robot

Suite Setup  Test Setup
Suite Teardown  Test Teardown
Test Teardown  Run keyword if test failed  Fatal Error  Step Failed

*** Variables ***
${quantity_of_games}  ${3}

*** Test Cases ***

Games From Random Genre
    ${page_object} =  Choose Random Category  ${page_object}
    Set Suite Variable  ${page_object}
    Check Current Genre  ${page_object}
    ${fetched_games} =  Get Games List  ${page_object}  ${quantity_of_games}
    Set Suite Variable  ${fetched_games}

Find Game From Fetched
    ${page_object}  ${suggested_game} =  Search Game From Fetched  ${page_object}  ${fetched_games}
    Set Suite Variable  ${suggested_game}
    ${game_from_gamepage} =  Get Game Info From Game Page  ${page_object}
    Set Suite Variable  ${game_from_gamepage}

Compare Fetched Information
    Compare Info  ${fetched_games}  ${suggested_game}  ${game_from_gamepage}