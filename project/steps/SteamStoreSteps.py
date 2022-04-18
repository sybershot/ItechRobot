import os
import random
import urllib.parse
from typing import List

from robot.api.deco import keyword
from robot.output.librarylogger import info
from smart_assertions import soft_assert, verify_expectations

from itechframework.modules.robot_browser.browser_element import BrowserElement
from project.entities.steam_game_info import SteamGameInfo
from project.page_objects.steam_game_page import SteamGamePage
from project.page_objects.steam_main_page import SteamMainPage
from project.page_objects.steam_store_page import SteamStorePage
from project.utils.steam_info_utils import SteamInfoGrabber


class SteamStoreSteps:
    STEAM_SUBGENRES_LOCATOR = './child::a[@class="popup_menu_item"]'

    @staticmethod
    @keyword(name="Choose random category")
    def choose_random_category():
        page = SteamMainPage()
        categories = page.get_categories()
        category = random.choice(categories)
        genres = category.find_elements('xpath', SteamStoreSteps.STEAM_SUBGENRES_LOCATOR)
        genre = random.choice(genres)
        genre_link = os.path.dirname(urllib.parse.urlsplit(genre.get_attribute('href')).path)
        info(f'Got expected genre url: {genre_link}')
        genre = BrowserElement('xpath', f'//a[contains(@href,{genre_link!r})]')
        genre.click_element()
        return genre_link

    @staticmethod
    @keyword(name="Check current genre")
    def get_genre_name(expected_genre):
        page = SteamStorePage()
        page.browser.wait_until_visible('xpath', '//div[@class="tab_content_ctn sub"]')
        current_location = page.browser.get_location()
        info(f'Checking {expected_genre!r} in {current_location!r}')
        assert expected_genre in current_location

    @staticmethod
    @keyword(name="Get games list")
    def get_games_list(quantity):
        page = SteamStorePage()
        games_list = page.get_game_items(quantity)
        games_data = [SteamInfoGrabber.get_steam_game(i) for i in games_list]
        info(f'Fetched games: {games_data!r}')
        return games_data

    @staticmethod
    @keyword(name="Search game from fetched")
    def find_game_from_fetched(fetched_games):
        page = SteamStorePage()
        fetched_game: SteamGameInfo = fetched_games[0]
        info(f'Searching for {fetched_game} through search bar')
        game = page.search(fetched_game.game_title)
        return game

    @staticmethod
    @keyword(name="Get game info from game page")
    def get_game_info_from_game_page():
        page = SteamGamePage()
        game_info = SteamInfoGrabber.get_steam_game(page.browser.find_element_or_raise(page.purchase_game_block.by,
                                                                                       page.purchase_game_block.locator))
        info(f'Parsed game: {game_info!r}')
        return game_info

    @staticmethod
    @keyword(name="Compare info")
    def compare_games(from_carousel: List[SteamGameInfo], suggested: SteamGameInfo, game_page: SteamGameInfo):
        game_from_carousel = from_carousel[0]
        info(f'Passed Game information:\n'
             f'From main page: {game_from_carousel!r}\n'
             f'From suggested games list: {suggested!r}\n'
             f'From game page: {game_page!r}')
        soft_assert(game_from_carousel.game_title == suggested.game_title == game_page.game_title,
                    "Titles are not equal!")
        soft_assert(game_from_carousel.final_price == suggested.final_price == game_page.final_price,
                    "Prices are not equal!")
        verify_expectations()
