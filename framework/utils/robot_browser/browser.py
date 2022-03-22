from robot.api.deco import keyword
from robot.api.logger import info
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.constants import TIMEOUT


class Browser:
    def __init__(self, driver, name):
        self.driver: WebDriver = driver
        self.name = name

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

    @keyword(name='Wait until visible')
    def wait_until_visible(self, by, locator):
        info(f'Waiting until {by!r} {locator!r} is visible')
        return WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located((by, locator)))

    @keyword(name='Capture page screenshot')
    def capture_page_screenshot(self, file_name):
        image_path = file_name + '.png'
        self.driver.save_screenshot(image_path)
        info(f'<img src="{image_path}">', html=True)

    def find_elements(self, by, locator):
        info(f'Searching all elements by {by!r} {locator!r}')
        return self.driver.find_elements(by, locator)
