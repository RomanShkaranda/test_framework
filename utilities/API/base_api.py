import requests
from utilities.read_json import data_store


class BaseAPI:
    def __init__(self):
        self.__get_config = data_store()
        self.__base_url = self.__get_config.application_info['API_url']
        self.__user = 'admin'
        self.__headers = {"Authorization": f'{self.__get_config.application_info["token"]}'}
        self.__requests = requests


    def get(self, url, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.get(f'{self.__base_url}{url}', headers=headers)
        return response

    def post(self, url, body={}, headers=None):
        if headers is None:
            headers = self.__headers
        token = {"Authorization": f'{self.__get_config.application_info["token"]}'}
        response = self.__requests.post(f'{self.__base_url}{url}', headers=token, json=body)
        return response


