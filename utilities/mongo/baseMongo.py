import json
import pymongo
from CONSTANTS import ROOT_DIR
from utilities.configuration import Configuration


class BaseMongo:
    def __init__(self):
        self._client = pymongo.MongoClient(self.get_config().application_info["mongo_client"])
        self.mydb = self._client["schools"]
        self.mycol = []

    @staticmethod
    def get_config():
        with open(f'{ROOT_DIR}/configurations/configuration.json') as f:
            data = f.read()
            json_to_dict = json.loads(data)

            config = Configuration(**json_to_dict)
            return config

    def insert_one(self, item):
        self.mycol.insert_one(item)

    def find_one(self):
        return self.mycol.find_one()

    def find_all(self):
        all_list = []
        for i in self.mycol.find():
            all_list.append(i)
        return all_list

    def insert_many(self, insert_list: list):
        self.mycol.insert_many(insert_list)
        print('inserted list: ', insert_list)

    def delete_all(self):
        deleted = self.mycol.delete_many({})
        print(deleted.deleted_count, 'documents deleted.')

