from itechframework.modules.base_page.base_page import BasePage
from itechframework.modules.robot_browser.browser_element import BrowserElement
from itechframework.modules.utils.download_utils import DownloadUtils


class SteamDownloadPage(BasePage):
    def __init__(self):
        super().__init__()
        self.download_button = BrowserElement('xpath', '//a[@class="about_install_steam_link"]')

    def get_download_link(self):
        return self.download_button.get_attribute('href')

    def download(self, timeout=10):
        url = self.get_download_link()
        DownloadUtils.download(url, timeout, "Steam Installer.exe")
