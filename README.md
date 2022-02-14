# ItechRobot
Simple task using SeleniumLibrary and RobotFramework.

Test case:

1. Open "Steam" main page.
2. Click login element on the main page.
3. Enter invalid credentials.
4. Click login button.
5. Assert account invalid dialog.

# Requirements
- Robot Framework 4.1.3
- Webdriver Manager 3.5.2

Dependencies are listed in requirements.txt.

# Usage
Launch `login_test.robot` from `./project/tests/` directory with
`-V configuration/constants.py project/tests/login_test.robot` arguments.
