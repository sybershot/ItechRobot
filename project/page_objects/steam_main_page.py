from typing import List

from itechframework.modules.base_page.base_page import BasePage
from itechframework.modules.robot_browser.browser_element import BrowserElement
from project.utils.steam_info_utils import SteamInfoGrabber


class SteamMainPage(BasePage):
    STEAM_GENRES_LOCATOR = '//div[@class="popup_genre_expand_content responsive_hidden" and @data-genre-group and ' \
                           'not(@data-genre-group="themes") and not(@data-genre-group="social_and_players")]'

    def __init__(self):
        super().__init__()
        self.login_button = self.browser.find_element_or_raise('xpath', '//a[@class="global_action_link"]')
        self.install_steam_button = self.browser.find_element_or_raise('xpath',
                                                                       '//a[@class="header_installsteam_btn_content"]')
        self.steam_genre_menu = self.browser.find_element_or_raise('xpath', '//div[@id="genre_tab"]')
        self.search_bar = self.browser.find_element_or_raise('xpath', '//input[@id="store_nav_search_term"]')

    def click_login(self):
        self.login_button.click_element()

    def click_install_steam(self):
        self.install_steam_button.click_element()

    def get_categories(self):
        self.steam_genre_menu.move_to_element()
        self.browser.wait_until_visible('xpath', SteamMainPage.STEAM_GENRES_LOCATOR)
        return self.browser.find_elements('xpath', SteamMainPage.STEAM_GENRES_LOCATOR)

    def search(self, game_title):
        self.search_bar.move_to_element()
        self.search_bar.click_element()
        self.search_bar.input_text(game_title)
        self.browser.wait_until_visible('xpath', '//div[contains(@class, "search_suggest")]')
        game = self.browser.find_element_or_raise('xpath', '//a[contains(@class, "match")]')
        result = SteamInfoGrabber.get_steam_game(game)
        game.click_element()
        return result

