import json

from api_collection.data.user_data import User
from utilities.API.BaseAPI import BaseAPI


class UsersAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = 'public/v2/users'

    def get_user_by_id(self, user_id='3404'):
        return self.get(f'{self.__url}/{user_id}')

    def create_user(self):
        token = {"Authorization": "Bearer f17f3e0918e07151c1196b7dfbc4660cfd4598017a6dc9b03d8754759c442c3c"}
        body = User().get_dict()
        return self.post(f'{self.__url}', headers=token, body=body)


print(UsersAPI().create_user())
