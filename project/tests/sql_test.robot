*** Settings ***
Documentation  Verifies ability to send SQL requests using python
Default Tags  Smoke

Variables  configuration/constants.py
Library  project/steps/SQLSteps.py

*** Test Cases ***
Fetch All From DB
    ${connection} =  Connect To DB
    Fetch All Games  ${connection}

