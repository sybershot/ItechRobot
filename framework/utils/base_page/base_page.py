from framework.utils.browser_manager.browser import Browser


class BasePage:
    def __init__(self, browser: Browser):
        self.browser = browser


