from itechframework.modules.base_page.base_page import BasePage
from project.utils.download_utils import DownloadUtils


class SteamDownloadPage(BasePage):
    DOWNLOAD_BUTTON_LOCATOR = '//a[@class="about_install_steam_link"]'

    def __init__(self):
        super().__init__()
        self.download_button = self.browser.find_element_or_raise('xpath', SteamDownloadPage.DOWNLOAD_BUTTON_LOCATOR)

    def get_download_link(self):
        element = self.browser.driver.find_element(self.download_button.by, self.download_button.locator)
        return element.get_attribute('href')

    def download(self, timeout=10):
        url = self.get_download_link()
        DownloadUtils.download(url, timeout)
