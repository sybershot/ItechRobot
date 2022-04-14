*** Settings ***
Documentation  Verifies ability to download steam client app
Default Tags  Smoke

Resource  project/resource/Common.robot
Library  project.steps.SteamDownloadSteps

Suite Setup  Open Browser
Suite Teardown  Close Browser


*** Test Cases ***

Download Steam Client
    Go To Steam Page
    Go To Download Page
    Click Download Button