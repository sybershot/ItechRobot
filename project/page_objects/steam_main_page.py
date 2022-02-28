from typing import List

from selenium.webdriver.remote.webelement import WebElement
from framework.utils.base_page.base_page import BasePage

LOGIN_LINK_LOCATOR = '//a[@class="global_action_link"]'
DOWNLOAD_LINK_LOCATOR = '//a[@class="header_installsteam_btn_content"]'
STEAM_GENRES_LOCATOR = '//div[@class="popup_genre_expand_content responsive_hidden" and @data-genre-group and ' \
                       'not(@data-genre-group="themes") and not(@data-genre-group="social_and_players")]'
STEAM_GENRE_MENU_LOCATOR = '//div[@id="genre_tab"]'
STEAM_SEARCH_BAR_LOCATOR = '//input[@id="store_nav_search_term"]'
STEAM_SEARCH_SUGGEST_LOCATOR = '//div[contains(@class, "search_suggest")]'


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
