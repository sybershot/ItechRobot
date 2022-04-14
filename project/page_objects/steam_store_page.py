from typing import List

from project.page_objects.steam_main_page import SteamMainPage


class SteamStorePage(SteamMainPage):
    STEAM_STORE_GAMES_CAROUSEL_LOCATOR = '//div[@class="tab_content_section_ctn"]'
    STEAM_STORE_ITEM_LOCATOR = '//div[contains(@id, "NewReleasesRows")]/a[contains(@class, "tab_item")]'

    def __init__(self):
        super().__init__()

    def get_game_items(self, quantity):
        self.browser.wait_until_visible('xpath', SteamStorePage.STEAM_STORE_GAMES_CAROUSEL_LOCATOR)
        game_items: List = self.browser.find_elements('xpath', SteamStorePage.STEAM_STORE_ITEM_LOCATOR)
        return game_items[:quantity]
