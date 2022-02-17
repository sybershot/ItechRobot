from configuration.constants import USERNAME_FIELD_LOCATOR, PASSWORD_FIELD_LOCATOR, LOGIN_BUTTON_LOCATOR, \
    ERROR_MESSAGE_BOX_LOCATOR
from framework.utils.base_page.base_page import BasePage


class SteamLoginPage(BasePage):

    @property
    def username_input(self):
        return self.browser.find_element('xpath', USERNAME_FIELD_LOCATOR)

    @property
    def password_input(self):
        return self.browser.find_element('xpath', PASSWORD_FIELD_LOCATOR)

    @property
    def login_button(self):
        return self.browser.find_element('xpath', LOGIN_BUTTON_LOCATOR)

    @property
    def error_message_box(self):
        return self.browser.find_element('xpath', ERROR_MESSAGE_BOX_LOCATOR)

    def login(self, login, password):
        self.username_input.send_keys(login)
        self.password_input.send_keys(password)
        self.login_button.click()
