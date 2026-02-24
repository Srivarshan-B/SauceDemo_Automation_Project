import configparser
import os


class ConfigReader:

    def __init__(self):
        self.config = configparser.ConfigParser()

        # Get project root
        base_path = os.path.dirname(os.path.dirname(__file__))

        # Point to config/config.ini
        config_path = os.path.join(base_path, "config", "config.ini")

        self.config.read(config_path)

    def get(self, key):
        if self.config.has_option("DEFAULT", key):
            return self.config.get("DEFAULT", key)
        else:
            raise Exception(f"{key} not found in config.ini")