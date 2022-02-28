from framework.utils.base_page.base_page import BasePage

LOGIN_BUTTON_LOCATOR = '//button[@class="btn_blue_steamui btn_medium login_btn"]'
USERNAME_FIELD_LOCATOR = '//input[@id="input_username"]'
PASSWORD_FIELD_LOCATOR = '//input[@id="input_password"]'
ERROR_MESSAGE_BOX_LOCATOR = '//*[@id="error_display"]'
ERROR_MESSAGE_VISIBLE_LOCATOR = '//*[@id="error_display" and @style=""]'


class SteamLoginPage(BasePage):

    @property
    def username_input(self):
        return 'xpath', USERNAME_FIELD_LOCATOR

    @property
    def password_input(self):
        return 'xpath', PASSWORD_FIELD_LOCATOR

    @property
    def login_button(self):
        return 'xpath', LOGIN_BUTTON_LOCATOR

    @property
    def error_message_box(self):
        return 'xpath', ERROR_MESSAGE_BOX_LOCATOR

    @property
    def error_message_visible(self):
        return 'xpath', ERROR_MESSAGE_VISIBLE_LOCATOR

    def login(self, login, password):
        self.browser.input_text(*self.username_input, login)
        self.browser.input_text(*self.password_input, password)
        self.browser.click_element(*self.login_button)

    def wait_until_error_message_visible(self):
        self.browser.wait_until_visible(*self.error_message_visible)
