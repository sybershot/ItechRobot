import os
import random
import re
import urllib.parse
from typing import List
from robot.api.deco import keyword
from robot.output.librarylogger import info
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations
from framework.utils.robot_browser.browser_element import BrowserElement
from project.dataclasses.steam_game_info import SteamGameInfo, PRICE_PATTERN
from project.page_objects.steam_game_page import SteamGamePage
from project.page_objects.steam_main_page import SteamMainPage
from project.page_objects.steam_store_page import SteamStorePage


class SteamStoreSteps:
    GAME_MATCH_LOCATOR = '//a[contains(@class, "match")]'
    STEAM_SUBGENRES_LOCATOR = './child::a[@class="popup_menu_item"]'

    @staticmethod
    @keyword(name="Choose random category")
    def choose_random_category(page: SteamMainPage):
        genre = random.choice(page.get_genres())
        subgenres = genre.find_elements('xpath', SteamStoreSteps.STEAM_SUBGENRES_LOCATOR)
        subgenre = random.choice(subgenres)
        genre_link = subgenre.element.get_attribute('href')
        genre_link = os.path.dirname(urllib.parse.urlsplit(genre_link).path)
        info(str(genre_link))
        subgenre.click_element()

        return SteamStorePage(page.browser, genre_link)

    @staticmethod
    @keyword(name="Check current genre")
    def get_genre_name(page: SteamStorePage):
        info(f'Checking {page.current_genre!r} in {page.expected_genre_link!r}')
        assert page.current_genre in page.expected_genre_link

    @staticmethod
    @keyword(name="Get games list")
    def get_games_list(page: SteamStorePage, quantity):
        games_list: List[WebElement] = page.get_game_items(quantity)
        games_data = [SteamGameInfo.get_steam_game(i) for i in games_list]
        info(f'Fetched games: {games_data!r}')
        return games_data

    @staticmethod
    @keyword(name="Search game from fetched")
    def find_game_from_fetched(page: SteamStorePage, fetched_games):
        fetched_game: SteamGameInfo = fetched_games[0]
        info(f'Searching for {fetched_game} through search bar')
        page.search_bar.click_element()
        page.search_bar.input_text(fetched_game.game_title)
        page.browser.wait_until_visible('xpath', SteamStorePage.STEAM_SEARCH_SUGGEST_LOCATOR)
        game_match = BrowserElement.from_locator('xpath', SteamStoreSteps.GAME_MATCH_LOCATOR)
        suggested_game_name, final_price = game_match.element.text.split("\n")
        if fetched_game.final_price != 0.0:
            final_price = float(re.search(PRICE_PATTERN, final_price.replace(*SteamGameInfo.COMMA_DOT))[0])
        else:
            final_price = 0.0
        game_match.click_element()
        return SteamGamePage(page.browser), SteamGameInfo(suggested_game_name, [], final_price, final_price, 0.0)

    @staticmethod
    @keyword(name="Get game info from game page")
    def get_game_info_from_game_page(page: SteamGamePage):
        game_info = SteamGameInfo.get_steam_game(page.purchase_game_block)
        info(f'Got an info for game: {game_info!r}')
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
