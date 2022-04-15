*** Settings ***
Documentation  Verifies ability to send SQL requests using python
Default Tags  Smoke

Variables  project/resource/resource.robot
Library  project/steps/SQLSteps.py

*** Test Cases ***
Fetch All From DB
    ${connection} =  Connect To DB
    Fetch All Games  ${connection}

