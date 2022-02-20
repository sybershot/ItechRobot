from configuration.constants import LOGIN_LINK_LOCATOR
from framework.utils.base_page.base_page import BasePage


class SteamMainPage(BasePage):

    @property
    def login_button(self):
        return 'xpath', LOGIN_LINK_LOCATOR

    def click_login(self):
        self.browser.click_element(*self.login_button)

    @property
    def install_steam_button(self):
        return self.browser.find_element('xpath', "pass")  # TODO: Case 2 for steam.
