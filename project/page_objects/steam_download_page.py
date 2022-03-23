import os
import pathlib

from requests import get
from robot.output.librarylogger import info

from configuration.constants import DOWNLOADS_PATH
from framework.utils.base_page.base_page import BasePage
from framework.utils.robot_browser.browser import Browser
from framework.utils.robot_browser.browser_element import BrowserElement

DOWNLOAD_BUTTON_LOCATOR = '//a[@class="about_install_steam_link"]'


class SteamDownloadPage(BasePage):

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self._download_button = BrowserElement.from_locator('xpath', DOWNLOAD_BUTTON_LOCATOR)
        self.download_link = self._download_button.element.get_attribute('href')

    def download(self):
        if not pathlib.Path(DOWNLOADS_PATH).exists():
            os.mkdir(pathlib.Path(DOWNLOADS_PATH))
        file_path = pathlib.Path(DOWNLOADS_PATH, "SteamSetup.exe")
        res = get(self.download_link)
        if res.status_code == 200:
            info("Successfully downloaded steam installer.")
            with open(file_path, "wb") as installer:
                installer.write(res.content)
        else:
            raise Exception("Failed to download steam installer!")
