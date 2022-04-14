import json
import os.path
import re

from project.configuration.constants import CREDENTIALS_PATH


class JsonLoader:
    file_path = os.path.join(CREDENTIALS_PATH, "credentials.json")

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
            kv = re.search(r'(\w+).(\w+)', key)
            return json_data[kv[1]][kv[2]]
