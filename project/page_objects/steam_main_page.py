from typing import List

from selenium.webdriver.remote.webelement import WebElement

from configuration.constants import LOGIN_LINK_LOCATOR, DOWNLOAD_LINK_LOCATOR, STEAM_GENRES_LOCATOR, \
    STEAM_GENRE_MENU_LOCATOR, STEAM_SEARCH_BAR_LOCATOR, STEAM_SEARCH_SUGGEST_LOCATOR
from framework.utils.base_page.base_page import BasePage


class SteamMainPage(BasePage):

    @property
    def login_button(self):
        return 'xpath', LOGIN_LINK_LOCATOR

    @property
    def install_steam_button(self):
        return 'xpath', DOWNLOAD_LINK_LOCATOR

    @property
    def steam_genres_items(self):
        return 'xpath', STEAM_GENRES_LOCATOR

    @property
    def steam_genre_menu(self):
        return 'xpath', STEAM_GENRE_MENU_LOCATOR

    @property
    def search_bar(self):
        return 'xpath', STEAM_SEARCH_BAR_LOCATOR

    @property
    def search_suggest(self):
        return 'xpath', STEAM_SEARCH_SUGGEST_LOCATOR

    def click_login(self):
        self.browser.click_element(*self.login_button)

    def click_install_steam(self):
        self.browser.click_element(*self.install_steam_button)

    def get_genres(self) -> List[WebElement]:
        return self.browser.find_elements(*self.steam_genres_items)
