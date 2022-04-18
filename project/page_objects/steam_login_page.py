from itechframework.modules.base_page.base_page import BasePage
from itechframework.modules.robot_browser.browser_element import BrowserElement


class SteamLoginPage(BasePage):
    LOGIN_BUTTON_LOCATOR = '//button[@class="btn_blue_steamui btn_medium login_btn"]'
    USERNAME_FIELD_LOCATOR = '//input[@id="input_username"]'
    PASSWORD_FIELD_LOCATOR = '//input[@id="input_password"]'
    ERROR_MESSAGE_BOX_LOCATOR = '//*[@id="error_display"]'
    ERROR_MESSAGE_VISIBLE_LOCATOR = '//*[@id="error_display" and @style=""]'

    def __init__(self):
        super().__init__()
        self.username_input = BrowserElement('xpath', SteamLoginPage.USERNAME_FIELD_LOCATOR)
        self.password_input = BrowserElement('xpath', SteamLoginPage.PASSWORD_FIELD_LOCATOR)
        self.login_button = BrowserElement('xpath', SteamLoginPage.LOGIN_BUTTON_LOCATOR)
        self.error_message_box = BrowserElement('xpath', SteamLoginPage.ERROR_MESSAGE_BOX_LOCATOR)

    def login(self, login, password):
        self.username_input.input_text(login)
        self.password_input.input_text(password)
        self.login_button.click_element()

    def wait_until_error_message_visible(self):
        self.browser.wait_until_visible('xpath', SteamLoginPage.ERROR_MESSAGE_VISIBLE_LOCATOR)
