from robot.api.deco import keyword
from robot.api.logger import info, debug, error
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIMEOUT
from framework.utils.drivermanager.driver_manager import BrowserManager


class ElementNotFound(Exception):
    pass


class RobotBrowser:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, browser_type):
        self.driver: WebDriver = BrowserManager.get_browser(browser_type)

    def _find_element_or_raise(self, by, locator):
        info(f'Searching element {(by, locator)!r}')
        if element := self.driver.find_element(by, locator):
            return element
        else:
            raise ElementNotFound(f'Failed to find element {(by, locator)!r}!')

    @keyword(name='Wait until element')
    def wait_until_element(self, by, locator):
        info(f'Waiting for {(by, locator)!r}')
        if element := WebDriverWait(self.driver, TIMEOUT).until(EC.presence_of_element_located((by, locator))):
            debug(f'Successfully located {(by, locator)!r}')
            return element
        else:
            raise ElementNotFound(f'Failed to find element {(by, locator)!r}!')

    @keyword(name='Close browser')
    def close_browser(self):
        self.driver.quit()

    @keyword(name='Get location')
    def get_location(self):
        return self.driver.current_url

    @keyword(name='Go to')
    def go_to(self, url):
        info(f'Loading {url}')
        self.driver.get(url)

    @keyword(name='Input text')
    def input_text(self, by, locator, text):
        info(f'Sending {text!r} to {(by, locator)!r}')
        self._find_element_or_raise(by, locator).send_keys(text)

    @keyword(name='Click element')
    def click_element(self, by, locator):
        info(f'Clicking {(by, locator)!r}')
        self._find_element_or_raise(by, locator).click()

    @keyword(name='Wait until visible')
    def wait_until_visible(self, by, locator):
        info(f'Waiting until {(by, locator)!r} is visible')
        WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located((by, locator)))

    @keyword(name='Capture page screenshot')
    def capture_page_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)
