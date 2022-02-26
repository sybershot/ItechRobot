from robot.output.librarylogger import info, error

from configuration.constants import DOWNLOAD_BUTTON_LOCATOR
from framework.utils.base_page.base_page import BasePage
from requests import get


class SteamDownloadPage(BasePage):

    @property
    def download_button(self):
        return 'xpath', DOWNLOAD_BUTTON_LOCATOR

    def get_download_link(self):
        return self.browser.find_element(*self.download_button).get_attribute('href')

    def download(self):
        res = get(self.get_download_link())
        if res.status_code == 200:
            info("Successfully downloaded steam installer.")
        else:
            raise Exception("Failed to download steam installer!")