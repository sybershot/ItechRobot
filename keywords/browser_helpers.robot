*** Settings ***
Library  SeleniumLibrary


*** Keywords ***
Open Firefox Browser
    Open Browser  executable_path=utils/drivers/geckodriver.exe  service_log_path=/dev/null
