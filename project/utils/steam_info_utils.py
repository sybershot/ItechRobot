import re

from robot.api.logger import info
from selenium.webdriver.remote.webelement import WebElement

from project.entities.steam_game_info import SteamGameInfo

PRICE_PATTERN = r"[-+]?(\d*\.?\d+|\d+)"


class SteamInfoGrabber:
    DISCOUNT_PRICES_LOCATOR = './/div[@class="discount_prices"]'

    @staticmethod
    def get_steam_game(web_element: WebElement):
        orig_price = 0.0
        final_price = 0.0
        discount = 0.0
        if game_name_element := web_element.find_elements('xpath', './/div[@class="tab_item_name"]'):
            name = game_name_element[0].text
        elif game_name_element := web_element.find_elements('xpath', '//div[@class="apphub_AppName"]'):
            name = game_name_element[0].text
        else:
            name = web_element.find_element('xpath', '//div[@class="match_name"]').text

        platform_elements = web_element.find_elements('xpath', './/*/child::span[contains(@class, "platform_img")]')
        supported_os = [i.get_attribute('class').split()[-1] for i in platform_elements]

        if game_item := web_element.find_elements('xpath', './/div[@class="discount_pct"]'):
            discount_text = web_element.find_element('xpath', SteamInfoGrabber.DISCOUNT_PRICES_LOCATOR).text
            info(f"Trying to unpack {discount_text!r}")
            orig_price, final_price = discount_text.split("\n")
            orig_price = float(re.search(PRICE_PATTERN, orig_price.replace(',', '.'))[0])
            final_price = float(re.search(PRICE_PATTERN, final_price.replace(',', '.'))[0])
            discount = abs(float(game_item[0].text[:-1]) / 100)  # Converts discount percent to price multiplier
        else:
            # Checking if the game has price element
            if dirty_price := web_element.find_elements('xpath', SteamInfoGrabber.DISCOUNT_PRICES_LOCATOR):
                info(f'Found price from game carousel {dirty_price}')
            # This check is needed when searching for a game price when on game page
            elif dirty_price := web_element.find_elements('xpath',
                                                          './/child::div[contains(@class, "game_purchase_price")]'):
                info(f'Found price from game page {dirty_price}')
            # Finding game's price from search suggest
            elif dirty_price := web_element.find_elements('xpath', '//div[@class="match_price"]'):
                info(f'Found price from game suggest {dirty_price}')

            dirty_price = dirty_price[0].text
            # Checking if the game is not free, it should fail if no price has been found
            cleaned_price = re.search(PRICE_PATTERN, dirty_price.replace(',', '.'))
            if cleaned_price is not None:
                final_price = float(cleaned_price[0])
                orig_price = final_price
        return SteamGameInfo(name, supported_os, orig_price, final_price, discount)
