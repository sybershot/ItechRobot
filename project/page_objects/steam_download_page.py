import os
import time

from requests import get
from robot.output.librarylogger import info

from project.configuration.constants import DOWNLOADS_PATH
from itechframework.modules.base_page.base_page import BasePage


class SteamDownloadPage(BasePage):
    DOWNLOAD_BUTTON_LOCATOR = '//a[@class="about_install_steam_link"]'

    def __init__(self):
        super().__init__()
        self.download_button = self.browser.find_element_or_raise('xpath', SteamDownloadPage.DOWNLOAD_BUTTON_LOCATOR)

    def get_download_link(self):
        return self.download_button.element.get_attribute('href')

    def download(self, timeout=10):
        file_path = os.path.join(DOWNLOADS_PATH, "steam_installer.exe")
        start = time.time()
        with get(self.get_download_link(), stream=True) as r:
            r.raise_for_status()
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if time.time() < start + timeout:
                        f.write(chunk)
                    else:
                        raise Exception(f'Timeout: download took too long!')
        info("Successfully downloaded steam installer.")
