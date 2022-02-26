import os
import random
import re
import urllib.parse
from typing import List

from robot.api.deco import keyword
from robot.output.librarylogger import info
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from configuration.constants import STEAM_SUBGENRES_LOCATOR
from project.dataclasses.steam_game_info import SteamGameInfo, PRICE_PATTERN
from project.page_objects.steam_game_page import SteamGamePage
from project.page_objects.steam_main_page import SteamMainPage
from project.page_objects.steam_store_page import SteamStorePage

GAME_MATCH_LOCATOR = 'xpath', '//a[contains(@class, "match")]'


class SteamStoreSteps:

    @staticmethod
    @keyword(name="Choose random category")
    def choose_random_category(page: SteamMainPage):
        menu_element = page.browser.find_element(*page.steam_genre_menu)
        hover: ActionChains = ActionChains(page.browser.driver).move_to_element(menu_element)
        hover.perform()
        page.browser.wait_until_visible(*page.steam_genres_items)
        genres = page.get_genres()
        genre = random.choice(genres)

        subgenres = genre.find_elements('xpath', STEAM_SUBGENRES_LOCATOR)
        subgenre = random.choice(subgenres)
        genre_link = subgenre.get_attribute('href')
        genre_link = os.path.dirname(urllib.parse.urlsplit(genre_link).path)
        info(str(genre_link))
        subgenre.click()

        return SteamStorePage(page.browser, genre_link)

    @staticmethod
    @keyword(name="Check current genre")
    def get_genre_name(page: SteamStorePage):
        info(f'Checking {page.current_genre!r} is equal to {page.expected_genre_link!r}')
        assert page.current_genre == page.expected_genre_link

    @staticmethod
    @keyword(name="Get games list")
    def get_games_list(page: SteamStorePage, quantity):
        games_list = page.get_game_items(quantity)
        games_data = [SteamGameInfo.get_steam_game(i) for i in games_list]
        info(f'Fetched games: {games_data!r}')
        return games_data

    @staticmethod
    @keyword(name="Search game from fetched")
    def find_game_from_fetched(page: SteamStorePage, fetched_games):
        fetched_game: SteamGameInfo = fetched_games[0]
        info(f'Searching for {fetched_game} through search bar')
        search_bar: WebElement = page.browser.find_element(*page.search_bar)
        search_bar.click()
        search_bar.send_keys(fetched_game.game_title)
        page.browser.wait_until_visible(*page.search_suggest)
        game_match = page.browser.find_element(*GAME_MATCH_LOCATOR)
        suggested_game_name, final_price = game_match.text.split("\n")
        if fetched_game.final_price != 0.0:
            final_price = float(re.search(PRICE_PATTERN, final_price.replace(',', '.'))[0])
        else:
            final_price = 0.0
        game_match.click()
        return SteamGamePage(page.browser), SteamGameInfo(suggested_game_name, [], final_price, final_price, 0.0)

    @staticmethod
    @keyword(name="Get game info from game page")
    def get_game_info_from_game_page(page: SteamGamePage):
        game_purchase_block_element = page.browser.wait_until_element(*page.purchase_game_block)
        game_info = SteamGameInfo.get_steam_game(game_purchase_block_element)
        info(f'Got an info for game: {game_info!r}')
        return game_info

    @staticmethod
    @keyword(name="Compare info")
    def compare_games(from_carousel: List[SteamGameInfo], suggested: SteamGameInfo, game_page: SteamGameInfo):
        game_from_carousel = SteamGameInfo.make_set(from_carousel[0])
        from_suggested = SteamGameInfo.make_set(suggested)
        from_game_page = SteamGameInfo.make_set(game_page)
        info(f'Passed Game information:\n'
             f'From main page: {game_from_carousel!r}\n'
             f'From suggested games list: {from_suggested!r}\n'
             f'From game page: {from_game_page!r}')
        if game_from_carousel == from_suggested == from_game_page:
            info("All of the fetched fetched data for game is equal!")
            return True
        else:
            return Exception("Some of the fetched data is not equal!")
