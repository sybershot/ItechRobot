from robot.api.logger import info, debug
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.constants import BROWSER_TYPE, TIMEOUT
from framework.utils.robot_browser.browser import Browser


class ElementNotFound(Exception):
    pass


class BrowserElement:
    def __init__(self, by, locator, browser: Browser):
        self._browser = browser
        self.by = by
        self.locator = locator
        self.element = self.find_element_or_raise(by, locator)

    def find_element_or_raise(self, by, locator) -> WebElement:
        debug(f'Searching element {by!r} {locator!r}')
        if element := WebDriverWait(self._browser.driver, TIMEOUT).until(EC.presence_of_element_located((by, locator))):
            return element
        else:
            raise ElementNotFound(f'Failed to find element {by!r} {locator!r}!')

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

