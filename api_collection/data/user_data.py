import json
import random
import string


class User:
    def __init__(self, **kwargs):
        self.id = 4934 if 'id' not in kwargs.keys() else kwargs['id']
        self.name = 'Deeptimoy Malik' if 'name' not in kwargs.keys() else kwargs['name']
        email_pref = ''.join(random.choice(string.ascii_letters) for _ in range(7))
        self.email = 'malik_deeptimoy@muller-abbott.info' if 'email' not in kwargs.keys() else f'{email_pref}@mail.com' if 'email' not in kwargs.keys() else kwargs['email']
        self.gender = 'male' if 'gender' not in kwargs.keys() else kwargs['gender']
        self.status = 'inactive' if 'status' not in kwargs.keys() else kwargs['status']

    def to_json(self):
        return json.dumps(self.__dict__)

    def get_dict(self):
        return self.__dict__
