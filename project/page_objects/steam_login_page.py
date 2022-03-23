from framework.utils.base_page.base_page import BasePage
from framework.utils.robot_browser.browser import Browser
from framework.utils.robot_browser.browser_element import BrowserElement

LOGIN_BUTTON_LOCATOR = '//button[@class="btn_blue_steamui btn_medium login_btn"]'
USERNAME_FIELD_LOCATOR = '//input[@id="input_username"]'
PASSWORD_FIELD_LOCATOR = '//input[@id="input_password"]'
ERROR_MESSAGE_BOX_LOCATOR = '//*[@id="error_display"]'
ERROR_MESSAGE_VISIBLE_LOCATOR = '//*[@id="error_display" and @style=""]'


class SteamLoginPage(BasePage):
    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.login_button = BrowserElement.from_locator('xpath', LOGIN_BUTTON_LOCATOR)
        self.username_input = BrowserElement.from_locator('xpath', USERNAME_FIELD_LOCATOR)
        self.password_input = BrowserElement.from_locator('xpath', PASSWORD_FIELD_LOCATOR)

    @property
    def error_message_box(self):
        return 'xpath', ERROR_MESSAGE_BOX_LOCATOR

    @property
    def error_message_visible(self):
        return 'xpath', ERROR_MESSAGE_VISIBLE_LOCATOR

    def login(self, login, password):
        self.username_input.input_text(login)
        self.password_input.input_text(password)
        self.login_button.click_element()

    def wait_until_error_message_visible(self):
        self.browser.wait_until_visible(*self.error_message_visible)
