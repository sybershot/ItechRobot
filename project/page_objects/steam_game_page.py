from itechframework.modules.base_page.base_page import BasePage


class SteamGamePage(BasePage):
    def __init__(self):
        super().__init__()
        self.purchase_game_block = self.browser.find_element_or_raise(
            'xpath', '//*/div/div[@class="game_area_purchase_game_wrapper"]')
