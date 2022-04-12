import json
import os.path

from configuration.constants import CREDENTIALS_PATH


class JsonLoader:

    file_path = os.path.join(CREDENTIALS_PATH, "credentials.json")

    @staticmethod
    def load(key):
        with open(JsonLoader.file_path, "r", encoding='utf-8') as cred_json:
            creds = json.load(cred_json)
            login = creds[key]["login"]
            password = creds[key]["password"]
        return login, password
