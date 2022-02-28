# ItechRobot
Simple task using SeleniumLibrary and RobotFramework.

# Test case #1
1. Open "Steam" main page.
2. Click login element on the main page.
3. Enter invalid credentials.
4. Click login button.
5. Assert account invalid dialog.

# Test case #2
1. Open "Steam" main page.
2. Check that main page was opened.
3. Click "install steam" button.
4. Download steam installer.
5. Check that file was successfully downloaded.

# Test case #3
1. Open "Steam" main page.
2. Select random genre from: "Action", "Role-playing", "Strategy", "Adventure & Casual", "Simulation", "Sports & Racing".
3. Check that correct game's genre was opened.
4. Store name, supported os, prices, discount of a game. (Data is stored for 1 to n games, where n - number of games, maximum is 15, defined within the robot file)
5. Find game fetched from previous step using search bar on the top of the page.
6. Store suggested game name and pricing.
7. Open game's page from step 6.
8. Check that game page was opened.
9. Store game's name, supported os, priced, discount.
10. Compare fetched results from: games list, suggested game and game page.

# Requirements
- Robot Framework 4.1.3
- Selenium 0.30
- Webdriver Manager 3.5.2

Dependencies are listed in requirements.txt.

# Usage
Tests (or tasks) are executed from the command line using the robot command or by executing the robot module directly like python -m robot or jython -m robot:
```
robot [path to .robot file]
```
All tests are located in `project/tests` folder.

Most of the parameters are located in `configuration` folder.