import configparser
from CONSTANTS import ROOT_DIR

abs_path = f'{ROOT_DIR}/configurations/configuration.ini'
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('application_info', 'base_url')

    @staticmethod
    def get_user_name():
        return config.get('user_info', 'user_name')

    @staticmethod
    def get_password():
        return config.get('user_info', 'password')

    @staticmethod
    def get_browser_id():
        return config.get('browser_info', 'browser_id')

    @staticmethod
    def get_first_name():
        return config.get('user_info', 'first_name')

    @staticmethod
    def get_last_name():
        return config.get('user_info', 'last_name')

    @staticmethod
    def get_postal_code():
        return config.get('user_info', 'postal_code')

