import re
from dataclasses import dataclass
from typing import List

from robot.api.logger import info
from selenium.webdriver.remote.webelement import WebElement

GAME_NAME_LOCATOR = 'xpath', './*/child::div[@class="tab_item_name"]'
APPHUB_GAME_NAME_LOCATOR = 'xpath', '//div[@class="apphub_AppName"]'
GAME_PRICE_APPHUB_LOCATOR = 'xpath', './/child::div[contains(@class, "game_purchase_price")]'
PLATFORM_LOCATOR = 'xpath', './/*/child::span[contains(@class, "platform_img")]'
DISCOUNT_PCT_LOCATOR = 'xpath', './/child::div[@class="discount_pct"]'
DISCOUNT_PRICES_LOCATOR = 'xpath', './/child::div[@class="discount_prices"]'
PRICE_PATTERN = r"[-+]?(\d*\.?\d+|\d+)"


@dataclass
class SteamGameInfo:
    game_title: str
    supported_os: List[str]
    original_price: float
    final_price: float
    discount: float

    @staticmethod
    def get_steam_game(web_element: WebElement):

        if game_name_element := web_element.find_elements(*GAME_NAME_LOCATOR):
            name = game_name_element[0].text
        else:
            name = web_element.find_element(*APPHUB_GAME_NAME_LOCATOR).text

        platform_elements = web_element.find_elements(*PLATFORM_LOCATOR)
        supported_os = [i.get_attribute('class').split()[-1] for i in platform_elements]
        if game_item := web_element.find_elements(*DISCOUNT_PCT_LOCATOR):
            discount_text = web_element.find_element(*DISCOUNT_PRICES_LOCATOR).text
            info(f"Trying to unpack {discount_text!r}")
            orig_price, final_price = discount_text.split("\n")
            orig_price = float(re.search(PRICE_PATTERN, orig_price.replace(',', '.'))[0])
            final_price = float(re.search(PRICE_PATTERN, final_price.replace(',', '.'))[0])
            discount = abs(float(game_item[0].text[:-1]) / 100)
        else:
            # Checking if the game has price element
            if dirty_price := web_element.find_elements(*DISCOUNT_PRICES_LOCATOR):
                dirty_price = dirty_price[0].text
            # This check is needed when searching for a game price when on game's page
            elif dirty_price := web_element.find_elements(*GAME_PRICE_APPHUB_LOCATOR):
                dirty_price = dirty_price[0].text
            else:
                dirty_price = 0.0

            # Checking if the game is not free
            cleaned_price = re.search(PRICE_PATTERN, dirty_price.replace(',', '.'))
            if cleaned_price is not None:
                final_price = float(cleaned_price[0])
                orig_price = final_price
            else:
                final_price = 0.0
                orig_price = final_price
            discount = 0.0
        return SteamGameInfo(name, supported_os, orig_price, final_price, discount)

    @staticmethod
    def make_set(game_info):
        return {game_info.game_title, game_info.final_price}
