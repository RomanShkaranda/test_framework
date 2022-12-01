import json

import requests


class BaseAPI:
    def __init__(self):
        self.__base_url = 'https://gorest.co.in/'
        self.__user = 'admin'
        self.__headers = {}
        self.__requests = requests

    def get(self, url, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.get(f'{self.__base_url}{url}', headers=headers)
        return response

    def post(self, url, body={}, headers=None):
        if headers is None:
            headers = self.__headers
        json_obj = json.dumps(body)
        response = self.__requests.post(f'{self.__base_url}{url}', headers=headers, json=body)
        return response

