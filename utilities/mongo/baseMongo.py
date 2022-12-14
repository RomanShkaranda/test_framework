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

    def insert_one(self, number, capacity, principle):
        self.mycol.insert_one({'number': number, 'capacity': capacity, 'principle': f'{principle}'})
        return print(f"created number {number}, capacity {capacity}, principle {principle}")

    def delete_by_number(self, number):
        self.mycol.delete_one({'number': number})

    def find_one(self):
        return self.mycol.find_one()

    def find_one_by_number(self, number):
        return print(self.mycol.find_one({'number': number}))

    def find_all(self):
        for i in self.mycol.find():
            print(i)

    def insert_many(self, insert_list):
        self.mycol.insert_many(insert_list)
        return print(f'inserted list {insert_list}')

    def delete_all(self):
        deleted = self.mycol.delete_many({})
        return print(deleted.deleted_count, 'documents deleted.')

