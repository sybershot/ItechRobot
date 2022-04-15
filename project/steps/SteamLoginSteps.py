from robot.api.deco import keyword

from itechframework.modules.utils.json_utils import JsonLoader
from project.page_objects.steam_login_page import SteamLoginPage
from project.page_objects.steam_main_page import SteamMainPage


class SteamLoginSteps:

    @staticmethod
    @keyword(name="Load from JSON file")
    def load_from_json_file(key):
        return JsonLoader.load(key)

    @staticmethod
    @keyword(name="Go to Login page")
    def go_to_login_page():
        page = SteamMainPage()
        page.click_login()

    @staticmethod
    @keyword(name="Login with credentials")
    def login_with_credentials(login, password):
        page = SteamLoginPage()
        page.login(login, password)

    @staticmethod
    @keyword(name="Wait until error visible")
    def wait_until_error_visible():
        page = SteamLoginPage()
        page.wait_until_error_message_visible()

    @staticmethod
    @keyword(name="Capture error message")
    def capture_error_message():
        page = SteamLoginPage()
        page.browser.capture_page_screenshot('invalid-credentials-attempt')
