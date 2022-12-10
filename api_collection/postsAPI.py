from utilities.API.base_api import BaseAPI


class PostsAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = 'public/v2/posts'

    def get_posts(self):
        return self.get(f'{self.__url}')
