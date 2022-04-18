from robot.api.logger import info, debug, warn
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains

from itechframework.configuration.config import BROWSER_TYPE
from itechframework.modules.utils import waituntiltrue
from itechframework.modules.utils.element_utils import update_if_stale


class BrowserElement:
    GOOGLE_AD_BANNER_CLOSE_LOCATOR = '//a[@id="close-fixedban"]'

    def __init__(self, by, locator):
        from itechframework.modules.browser_manager.browser_manager import BrowserManager

        self.browser = BrowserManager().get_browser(BROWSER_TYPE)
        self.by = by
        self.locator = locator

    @update_if_stale
    def input_text(self, text):
        element = self.browser.find_element_or_raise(self.by, self.locator)
        info(f'Sending {text!r} to {self.by!r} {self.locator!r}')
        element.send_keys(text)

    @update_if_stale
    def click_element(self, max_attempts=5):
        debug(f'Clicking {self.by!r} {self.locator!r}')
        element = self.browser.find_element_or_raise(self.by, self.locator)
        try:
            if self.wait_clickable():
                original_color = element.value_of_css_property('background-color')
                self.browser.driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)
                self.log_screenshot()
                self.browser.driver.execute_script("arguments[0].style.backgroundColor = arguments[1];",
                                                   element, original_color)
                self.browser.driver.execute_script("arguments[0].click();", element)
            else:
                return False
        except ElementClickInterceptedException:
            warn(f'Element by {self.by!r} {self.locator!r} is obstructed!'
                 f'Looking for advert banners and closing them if possible...')
            ad_banner_close = self.browser.find_elements('xpath', self.GOOGLE_AD_BANNER_CLOSE_LOCATOR)
            if ad_banner_close:
                for i in ad_banner_close:
                    i.click()
            element.click()

    def scroll_to_element(self):
        element = self.browser.find_element_or_raise(self.by, self.locator)
        debug(f'Scrolling to {self.by!r} {self.locator!r}')
        self.browser.driver.execute_script("arguments[0].scrollIntoView(false);", element)

    def move_to_element(self):
        element = self.browser.find_element_or_raise(self.by, self.locator)
        debug(f'moving to {self.by!r} {self.locator!r}')
        hover = ActionChains(self.browser.driver).move_to_element(element).perform()

    def log_screenshot(self):
        element = self.browser.find_element_or_raise(self.by, self.locator)
        info(f'<img src="data:image/png;base64, {element.screenshot_as_base64}">', html=True)

    @waituntiltrue
    def wait_clickable(self):
        element = self.browser.find_element_or_raise(self.by, self.locator)
        if element.is_displayed() and element.is_enabled():
            return True

    def update_element(self):
        return self.browser.find_element_or_raise(self.by, self.locator)

    def drag_and_drop(self, target):
        element = self.browser.find_element_or_raise(self.by, self.locator)
        info(f'Performing drag and drop of {self.by!r} {self.locator!r} to {target.by!r} {target.locator!r}')
        cursor: ActionChains = ActionChains(self.browser.driver).drag_and_drop(element, target)
        cursor.perform()

    def get_attribute(self, attr):
        element = self.browser.find_element_or_raise(self.by, self.locator)
        return element.get_attribute(attr)
