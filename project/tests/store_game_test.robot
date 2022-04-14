*** Settings ***
Documentation  Verifies ability to use store module
Default Tags  Smoke

Resource  project/resource/Common.robot
Library  project.steps.SteamStoreSteps

Suite Setup  Open Browser
Suite Teardown  Close Browser


*** Variables ***
${quantity_of_games}  ${3}

*** Test Cases ***

Test Game Store
    Go To Steam Page
    ${expected_genre} =  Choose Random Category
    Check Current Genre  ${expected_genre}
    ${games_from_carousel} =  Get Games List  ${quantity_of_games}
    ${game_from_searchbar} =  Search Game From Fetched  ${games_from_carousel}
    ${game_from_gamepage} =  Get Game Info From Game Page
    Compare Info  ${games_from_carousel}  ${game_from_searchbar}  ${game_from_gamepage}