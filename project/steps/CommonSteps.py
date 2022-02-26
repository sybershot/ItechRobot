from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from configuration.constants import STEAM_URL
from framework.utils.browser_manager.browser import Browser
from project.page_objects.steam_main_page import SteamMainPage


class CommonSteps:

    @staticmethod
    @keyword(name="Go to steam page")
    def go_to_steam_page(browser: Browser):
        browser.go_to(STEAM_URL)
        return SteamMainPage(browser)

    @staticmethod
    @keyword(name='Save page screenshot')
    def save_page_screenshot(page, file_name):
        page.save_screenshot(file_name)

    @staticmethod
    @keyword(name='Validate page is')
    def validate_page_is(browser: Browser, expected_url):
        BuiltIn().should_be_equal(browser.get_location(), expected_url)
