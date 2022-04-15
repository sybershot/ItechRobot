import os
import time

from requests import get
from robot.api.logger import info

from project.configuration.constants import DOWNLOADS_PATH


class DownloadUtils:

    @staticmethod
    def download(url, timeout, file_mane="content.exe"):
        file_path = os.path.join(DOWNLOADS_PATH, file_mane)
        start = time.time()
        with get(url, stream=True) as r:
            r.raise_for_status()
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if time.time() < start + timeout:
                        f.write(chunk)
                    else:
                        raise Exception(f'Timeout: download took too long!')
        info("Successfully downloaded file.")
