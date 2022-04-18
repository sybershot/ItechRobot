from typing import List

from project.page_objects.steam_main_page import SteamMainPage


class SteamStorePage(SteamMainPage):
    def __init__(self):
        super().__init__()

    def get_game_items(self, quantity):
        self.browser.wait_until_visible('xpath', '//div[@class="tab_content_section_ctn"]')
        game_items: List = self.browser.find_elements('xpath',
                                                      '//div[contains(@id, "NewReleasesRows")]/a[contains(@class, "tab_item")]')
        return game_items[:quantity]
