from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.wait import WebDriverWait

from configuration.constants import STEAM_URL, LOGIN_URL, TIMEOUT
from framework.utils.browser_manager.browser import Browser
from project.page_objects.steam_login_page import SteamLoginPage
from project.page_objects.steam_main_page import SteamMainPage
from selenium.webdriver.support import expected_conditions as EC


@keyword(name="Go to steam page")
def go_to_steam_page(browser: Browser):
    browser.go_to(STEAM_URL)
    return SteamMainPage(browser)


@keyword(name="Click login button")
def click_login_button(page: SteamMainPage):
    page.click_login()


@keyword(name='Validate page is')
def validate_page_is(browser: Browser, expected_url):
    BuiltIn().should_be_equal(browser.get_location(), expected_url)


@keyword(name="Go to Login page")
def go_to_steam_page(browser: Browser):
    browser.go_to(LOGIN_URL)
    return SteamLoginPage(browser)


@keyword(name="Login with credentials")
def login_with_credentials(page: SteamLoginPage, login, password):
    page.login(login, password)


@keyword(name="Capture error message")
def capture_error_message(page: SteamLoginPage):
    page.save_screenshot('invalid-credentials-attempt')

