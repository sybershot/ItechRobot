from typing import List

from selenium.webdriver.remote.webelement import WebElement
from framework.utils.base_page.base_page import BasePage


from framework.utils.robot_browser.browser import Browser
from framework.utils.robot_browser.browser_element import BrowserElement


class SteamMainPage(BasePage):

    LOGIN_LINK_LOCATOR = '//a[@class="global_action_link"]'
    DOWNLOAD_LINK_LOCATOR = '//a[@class="header_installsteam_btn_content"]'
    STEAM_GENRES_LOCATOR = '//div[@class="popup_genre_expand_content responsive_hidden" and @data-genre-group and ' \
                           'not(@data-genre-group="themes") and not(@data-genre-group="social_and_players")]'
    STEAM_GENRE_MENU_LOCATOR = '//div[@id="genre_tab"]'
    STEAM_SEARCH_BAR_LOCATOR = '//input[@id="store_nav_search_term"]'
    STEAM_SEARCH_SUGGEST_LOCATOR = '//div[contains(@class, "search_suggest")]'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.login_button = BrowserElement.from_locator('xpath', self.LOGIN_LINK_LOCATOR)
        self.install_steam_button = BrowserElement.from_locator('xpath', self.DOWNLOAD_LINK_LOCATOR)
        self.search_bar = BrowserElement.from_locator('xpath', self.STEAM_SEARCH_BAR_LOCATOR)
        self.steam_genre_menu = BrowserElement.from_locator('xpath', self.STEAM_GENRE_MENU_LOCATOR)

    def click_login(self):
        self.login_button.click_element()

    def click_install_steam(self):
        self.install_steam_button.click_element()

    def get_genres(self) -> list[BrowserElement]:
        self.steam_genre_menu.move_to_element()
        self.browser.wait_until_visible('xpath', self.STEAM_GENRES_LOCATOR)
        return self.browser.find_elements('xpath', self.STEAM_GENRES_LOCATOR)
