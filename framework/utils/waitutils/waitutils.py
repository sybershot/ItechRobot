import errno
import os
import time
from functools import wraps

class TimeoutError(Exception):
    pass

class WaitUtils:

    @staticmethod
    def waituntiltrue(func, seconds=5, error_message=os.strerror(errno.ETIME)):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            while time.time() < start + seconds:
                try:
                    if result := func(*args, **kwargs) != False:
                        return result
                    else:
                        raise Exception
                except:
                    continue
            raise TimeoutError(error_message)

        return wrapper


