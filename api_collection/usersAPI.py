from api_collection.data.user_data import User
from utilities.API.base_api import BaseAPI


class UsersAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = 'public/v2/users'

    def get_user_by_id(self, user_id=3404):
        return self.get(f'{self.__url}/{user_id}')

    def create_user(self):
        body = User(id=4934, name="Deeptimoy Malik", email="malik_deeptimoy@muller-abbott.info", gender="male", status="active")\
            .get_dict()
        return self.post(f'{self.__url}', body=body)