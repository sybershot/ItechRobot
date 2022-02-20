from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from framework.utils.browser_manager.browser import Browser
from project.page_objects.steam_login_page import SteamLoginPage
from project.page_objects.steam_main_page import SteamMainPage


class SteamLoginSteps:

    @staticmethod
    @keyword(name="Click login button")
    def click_login_button(page: SteamMainPage):
        page.click_login()

    @staticmethod
    @keyword(name='Validate page is')
    def validate_page_is(browser: Browser, expected_url):
        BuiltIn().should_be_equal(browser.get_location(), expected_url)

    @staticmethod
    @keyword(name="Go to Login page")
    def go_to_login_page(page: SteamMainPage):
        page.click_login()
        return SteamLoginPage(page.browser)

    @staticmethod
    @keyword(name="Login with credentials")
    def login_with_credentials(page: SteamLoginPage, login, password):
        page.login(login, password)

    @staticmethod
    @keyword(name="Wait until error visible")
    def wait_until_error_visible(page: SteamLoginPage):
        page.wait_until_error_message_visible()

    @staticmethod
    @keyword(name="Capture error message")
    def capture_error_message(page: SteamLoginPage):
        page.save_screenshot('invalid-credentials-attempt')
