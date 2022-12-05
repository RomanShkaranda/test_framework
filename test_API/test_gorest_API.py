from http import HTTPStatus
from api_collection.usersAPI import UsersAPI
from api_collection.postsAPI import PostsAPI


def test_get_user_by_id():
    user = UsersAPI().get_user_by_id('4934')
    expected_status_code = HTTPStatus.OK
    assert user.status_code == expected_status_code


def test_get_posts():
    posts = PostsAPI().get_posts()
    print(posts.status_code)
    assert posts.status_code == HTTPStatus.OK


def test_check_users(create_user):
    expected_user = create_user.get_dict()
    user = UsersAPI().get_user_by_id()
    actual_user = user.json()
    assert expected_user == actual_user

