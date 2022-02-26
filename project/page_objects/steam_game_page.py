from framework.utils.base_page.base_page import BasePage

PURCHASE_GAME_BLOCK_LOCATOR = '//*/div/div[@class="game_area_purchase_game_wrapper"]'
DISCOUNT_BLOCK_LOCATOR = './child::div[contains(@class, "discount_block")]'
NO_DISCOUNT_BLOCK_LOCATOR = '//*/div/div[@class="game_area_purchase_game_wrapper"]/*/*/div'


class SteamGamePage(BasePage):

    @property
    def purchase_game_block(self):
        return 'xpath', PURCHASE_GAME_BLOCK_LOCATOR

    @property
    def game_discount_block(self):
        return 'xpath', DISCOUNT_BLOCK_LOCATOR
