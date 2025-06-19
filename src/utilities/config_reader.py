# filepath: c:\Users\J\PycharmProjects\qaforge-projects\opencartlab-selenium-tests-python\src\utilities\config_reader.py

import os
import json

class ConfigReader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config_data.get(key, default)