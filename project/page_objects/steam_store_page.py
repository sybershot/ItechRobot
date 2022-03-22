import os
import urllib.parse
from typing import List

from framework.utils.robot_browser.browser import Browser
from framework.utils.robot_browser.browser_element import BrowserElement
from project.page_objects.steam_main_page import SteamMainPage


class SteamStorePage(SteamMainPage):
    STEAM_STORE_GAMES_CAROUSEL_LOCATOR = '//div[@class="tab_content_section_ctn"]'
    STEAM_STORE_ITEM_LOCATOR = '//div[contains(@id, "NewReleasesRows")]/a[contains(@class, "tab_item")]'

    def __init__(self, browser: Browser, genre):
        super().__init__(browser)
        self.expected_genre_link = genre
        self.game_carousel = BrowserElement('xpath', self.STEAM_STORE_GAMES_CAROUSEL_LOCATOR, browser)

    @property
    def current_genre(self):
        return os.path.dirname(urllib.parse.urlsplit(self.browser.get_location()).path)

    def get_game_items(self, quantity):
        game_items: List = self.browser.find_elements('xpath', self.STEAM_STORE_ITEM_LOCATOR)
        return game_items[:quantity]
