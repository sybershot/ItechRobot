from robot.api.logger import warn
from selenium.common.exceptions import StaleElementReferenceException


def update_if_stale(func, max_attempts=5):
    def wrapper(self, *args, **kwargs):
        attempt = 1
        while True:
            try:
                func(self, *args, **kwargs)
            except StaleElementReferenceException:
                warn(f'Tried to interact with stale element {self.by!r} {self.locator!r}! Updating...')
                if attempt >= max_attempts:
                    raise Exception(f'Maximum number of tries reached for {self.by!r} {self.locator!r}!')
                self.update_element()
                attempt += 1
                continue
            return func

    return wrapper