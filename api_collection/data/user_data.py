import json
import random
import string


class User:
    def __init__(self, **kwargs):
        email_pref = ''.join(random.choice(string.ascii_letters) for _ in range(7))
        self.email = f'{email_pref}@mail.com'
        self.name = 'Yakiv'
        self.gender = 'male'
        self.status = 'inactive'

    def to_json(self):
        return json.dumps(self.__dict__)

    def get_dict(self):
        return self.__dict__
