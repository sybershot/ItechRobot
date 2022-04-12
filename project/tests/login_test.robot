*** Settings ***
Documentation  Verifies error assertion with invalid login credentials
Default Tags  Smoke

Resource  itechframework/resource/Common.robot
Library  project.steps.SteamLoginSteps

Suite Setup  Open Browser
Suite Teardown  Close Browser

*** Test Cases ***

Log In With Invalid Credentials
    ${invalid_username}  ${invalid_password}  Load From JSON File  invalid
    Go To Steam Page
    Go To Login Page
    Login With Credentials  ${invalid_username}  ${invalid_password}
    Wait Until Error Visible
    Capture Error Message

