from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from itechframework.configuration.config import BROWSER_TYPE
from itechframework.modules.browser_manager.browser_manager import BrowserManager


class CommonSteps:

    @staticmethod
    @keyword(name="Go to steam page")
    def go_to_steam_page():
        browser = BrowserManager().get_browser(BROWSER_TYPE)
        browser.go_to('https://store.steampowered.com/')

    @staticmethod
    @keyword(name='Validate page is')
    def validate_page_is(expected_url):
        browser = BrowserManager().get_browser(BROWSER_TYPE)
        BuiltIn().should_be_equal(browser.get_location(), expected_url)

    @staticmethod
    @keyword(name="Get Browser")
    def get_browser(browser_type):
        return BrowserManager().get_browser(browser_type)

    @staticmethod
    @keyword(name="Destroy Browser")
    def destroy_browser(browser):
        BrowserManager().close_browser(browser)
