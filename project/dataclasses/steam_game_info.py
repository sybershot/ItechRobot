import re
from dataclasses import dataclass, field
from typing import List

from robot.api.logger import info
from selenium.webdriver.remote.webelement import WebElement

PRICE_PATTERN = r"[-+]?(\d*\.?\d+|\d+)"


@dataclass
class SteamGameInfo:
    game_title: str
    supported_os: List[str]
    original_price: float
    final_price: float
    discount: float

    GAME_NAME_SELECTOR = './*/child::div[@class="tab_item_name"]'
    APPHUB_GAME_NAME_SELECTOR = '//div[@class="apphub_AppName"]'
    GAME_PRICE_APPHUB_SELECTOR = './/child::div[contains(@class, "game_purchase_price")]'
    PLATFORM_SELECTOR = './/*/child::span[contains(@class, "platform_img")]'
    DISCOUNT_PCT_SELECTOR = './/child::div[@class="discount_pct"]'
    DISCOUNT_PRICES_SELECTOR = './/child::div[@class="discount_prices"]'
    COMMA_DOT = ',', '.'

    @staticmethod
    def find_price(price: str):
        return re.search(PRICE_PATTERN, price.replace(*SteamGameInfo.COMMA_DOT))

    @staticmethod
    def get_steam_game(web_element: WebElement):
        info(f'Recieved game item:\n')
        info(f'<img src="data:image/png;base64, {web_element.screenshot_as_base64}">', html=True)

        orig_price = 0.0
        final_price = 0.0
        discount = 0.0

        if game_name_element := web_element.find_elements('xpath', SteamGameInfo.GAME_NAME_SELECTOR):
            name = game_name_element[0].text
        else:
            name = web_element.find_element('xpath', SteamGameInfo.APPHUB_GAME_NAME_SELECTOR).text

        platform_elements = web_element.find_elements('xpath', SteamGameInfo.PLATFORM_SELECTOR)
        supported_os = [i.get_attribute('class').split()[-1] for i in platform_elements]

        #  Check if the game has discount
        if game_item := web_element.find_elements('xpath', SteamGameInfo.DISCOUNT_PCT_SELECTOR):
            discount_text = web_element.find_element('xpath', SteamGameInfo.DISCOUNT_PRICES_SELECTOR).text
            orig_price, final_price = discount_text.split("\n")
            orig_price = float(SteamGameInfo.find_price(orig_price)[0])
            final_price = float(SteamGameInfo.find_price(final_price)[0])
            discount = abs(float(game_item[0].text[:-1]) / 100)
        else:
            # Check if the game has price element
            if dirty_price := web_element.find_elements('xpath', SteamGameInfo.DISCOUNT_PRICES_SELECTOR):
                dirty_price = dirty_price[0].text
            # This check is needed when searching for a game price when on game's page
            elif dirty_price := web_element.find_elements('xpath', SteamGameInfo.GAME_PRICE_APPHUB_SELECTOR):
                dirty_price = dirty_price[0].text
            else:
                dirty_price = ""

            # Checking if the game is not free
            cleaned_price = SteamGameInfo.find_price(dirty_price)
            if cleaned_price is not None:
                final_price = float(cleaned_price[0])
                orig_price = final_price
        return SteamGameInfo(name, supported_os, orig_price, final_price, discount)
