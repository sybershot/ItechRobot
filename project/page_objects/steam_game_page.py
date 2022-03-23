from framework.utils.base_page.base_page import BasePage
from framework.utils.robot_browser.browser import Browser


from framework.utils.robot_browser.browser_element import BrowserElement


class SteamGamePage(BasePage):
    PURCHASE_GAME_BLOCK_SELECTOR = '//*/div/div[@class="game_area_purchase_game_wrapper"]'
    DISCOUNT_BLOCK_SELECTOR = './child::div[contains(@class, "discount_block")]'
    NO_DISCOUNT_BLOCK_SELECTOR = '//*/div/div[@class="game_area_purchase_game_wrapper"]/*/*/div'
    COMMENT_SECTION = '//*[@id="app_reviews_hash"]'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.purchase_game_block = BrowserElement.from_locator('xpath', self.PURCHASE_GAME_BLOCK_SELECTOR)
        self.game_discount_block = self._find_discount()

    def _find_discount(self):
        self.browser.wait_until_visible('xpath', self.COMMENT_SECTION)
        block = self.browser.find_elements('xpath', self.DISCOUNT_BLOCK_SELECTOR)
        return block
