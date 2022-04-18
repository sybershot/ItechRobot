from itechframework.modules.base_page.base_page import BasePage
from itechframework.modules.robot_browser.browser_element import BrowserElement


class SteamGamePage(BasePage):
    def __init__(self):
        super().__init__()
        self.purchase_game_block = BrowserElement('xpath', '//*/div/div[@class="game_area_purchase_game_wrapper"]')
