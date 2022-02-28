import os
import urllib.parse
from typing import List

from framework.utils.browser_manager.browser import Browser
from project.page_objects.steam_main_page import SteamMainPage

STEAM_STORE_GAMES_CAROUSEL_LOCATOR = '//div[@class="tab_content_section_ctn"]'
STEAM_STORE_ITEM_LOCATOR = '//div[contains(@id, "NewReleasesRows")]/a[contains(@class, "tab_item")]'


class SteamStorePage(SteamMainPage):

    def __init__(self, browser: Browser, genre):
        super().__init__(browser)
        self.expected_genre_link = genre

    @property
    def current_genre(self):
        return os.path.dirname(urllib.parse.urlsplit(self.browser.get_location()).path)

    def get_game_items(self, quantity):
        self.browser.wait_until_element('xpath', STEAM_STORE_GAMES_CAROUSEL_LOCATOR)
        game_items: List = self.browser.find_elements('xpath', STEAM_STORE_ITEM_LOCATOR)
        return game_items[:quantity]
