from robot.api.deco import keyword

from itechframework.modules.browser_manager.browser_manager import BrowserManager


class BrowManRobot:

    @staticmethod
    @keyword(name="Get Browser")
    def get_browser(browser_type):
        return BrowserManager().get_browser(browser_type)

    @staticmethod
    @keyword(name="Destroy Browser")
    def destroy_browser(browser):
        BrowserManager().close_browser(browser)
