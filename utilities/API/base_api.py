import json
import requests
from CONSTANTS import ROOT_DIR
from utilities.configuration import Configuration


class BaseAPI:
    def __init__(self):
        self.__base_url = self.get_config().application_info['API_url']
        self.__user = 'admin'
        self.__headers = {"Authorization": f'{self.get_config().application_info["token"]}'}
        self.__requests = requests

    @staticmethod
    def get_config():
        with open(f'{ROOT_DIR}/configurations/configuration.json') as f:
            data = f.read()
            json_to_dict = json.loads(data)

            config = Configuration(**json_to_dict)
            return config

    def get(self, url, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.get(f'{self.__base_url}{url}', headers=headers)
        return response

    def post(self, url, body={}, headers=None):
        if headers is None:
            headers = self.__headers
        token = {"Authorization": f'{self.get_config().application_info["token"]}'}
        response = self.__requests.post(f'{self.__base_url}{url}', headers=token, json=body)
        return response


