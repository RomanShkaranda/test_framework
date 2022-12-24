import json

from CONSTANTS import ROOT_DIR
from utilities.configuration import Configuration


def data_store():
    with open(f'{ROOT_DIR}/configurations/configuration.json') as f:
        data = f.read()
        json_to_dict = json.loads(data)

        config = Configuration(**json_to_dict)
        return config
