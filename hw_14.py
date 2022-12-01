from argparse import ArgumentParser
import json
import dicttoxml as dicttoxml
import names
import random
import datetime


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = ['male', 'female']
        self.birth_year = birth_year

    @staticmethod
    def convert_to_json():
        h1 = json.dumps(Human('asd', 'asd', 'asd', 'asd').__dict__)
        print(h1)

    @staticmethod
    def convert_to_xml():
        h2 = dicttoxml.dicttoxml(Human('asd', 'asd', 'asd', 'asd').__dict__)
        print(h2)


parser = ArgumentParser(description='Json/XML parser')
parser.add_argument('--datatype')
arguments = parser.parse_args()

if arguments.datatype.lower() == 'json_to_cli':
    Human.convert_to_json()
elif arguments.datatype.lower() == 'xml_to_cli':
    Human.convert_to_xml()


