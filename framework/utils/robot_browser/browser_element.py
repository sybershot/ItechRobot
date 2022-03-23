from robot.api.logger import info, debug
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configuration.constants import BROWSER_TYPE, TIMEOUT


class BrowserElement:
    def __init__(self, element, by, locator):
        from framework.utils.browser_manager.BrowserManager import BrowserManager

        self._browser = BrowserManager().get_browser(BROWSER_TYPE)
        self.element = element
        self.by = by
        self.locator = locator

    @classmethod
    def from_locator(cls, by, locator):
        from framework.utils.browser_manager.BrowserManager import BrowserManager

        browser = BrowserManager().get_browser(BROWSER_TYPE)
        return browser.find_element_or_raise(by, locator)

    def input_text(self, text):
        info(f'Sending {text!r} to {self.by!r} {self.locator!r}')
        self.element.send_keys(text)

    def click_element(self):
        screenshot = self.element.screenshot_as_base64
        debug(f'Clicking {self.by!r} {self.locator!r}')
        info(f'<img src="data:image/png;base64, {screenshot}">', html=True)
        self.element.click()

    def move_to_element(self):
        debug(f'Moving to {self.by!r} {self.locator!r}')
        hover: ActionChains = ActionChains(self._browser.driver).move_to_element(self.element)
        hover.perform()

    def find_elements(self, by, locator):
        return [BrowserElement(e, by, locator) for e in self.element.find_elements(by, locator)]

    def find_element(self, by, locator):
        return BrowserElement(self.element.find_element(by, locator), by, locator)

    def log_screenshot(self):
        info(f'<img src="data:image/png;base64, {self.element.screenshot_as_base64}">', html=True)
