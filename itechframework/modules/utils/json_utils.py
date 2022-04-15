import json
import os.path
import re

from project.configuration.constants import CREDENTIALS_PATH, LOCALE


class JsonLoader:
    file_path = os.path.join(CREDENTIALS_PATH, 'locale', LOCALE, "credentials.json")

    @staticmethod
    def load(key):
        """
        Loads data from JSON using '@key.value' syntax.
        :param key:
        :return:
        """
        with open(JsonLoader.file_path, "r", encoding='utf-8') as cred_json:
            json_data = json.load(cred_json)
        if key.startswith('@'):
            kv = re.finditer(r'(\w+)', key)
            val = None
            for i in kv:
                next_kv = next(kv)
                val = json_data[i[1]][next_kv[1]]
            return val
