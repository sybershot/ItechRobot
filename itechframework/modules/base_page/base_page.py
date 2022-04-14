from itechframework.configuration.config import BROWSER_TYPE
from itechframework.modules.browser_manager.browser_manager import BrowserManager


class BasePage:
    def __init__(self):
        self.browser = BrowserManager().get_browser(BROWSER_TYPE)
        self.url = self.browser.get_location

    def get_current_location(self):
        return self.url
