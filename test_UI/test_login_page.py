import string
import pytest
import random


@pytest.mark.smoke
def test_check_logo(open_login_page):
    assert open_login_page.is_login_logo_visible() is True, 'Login logo is not present'


@pytest.mark.regression
def test_is_login_button_present(open_login_page):
    login = open_login_page
    assert login.is_login_visible() is True, 'Login button is not visible'


@pytest.mark.smoke
def test_is_logged_in(open_main_page):
    main_page = open_main_page
    assert main_page.is_cart_visible() is True, 'Not logged in'


@pytest.mark.regression
def test_check_title(create_driver):
    assert create_driver.title == 'Swag Labs'


@pytest.mark.smoke
def test_invalid_login_data(open_login_page):
    user_name = ''.join(random.choice(string.ascii_letters) for i in range(5))
    password = ''.join(random.choice(string.ascii_letters) for i in range(10))
    login = open_login_page.login(user_name, password)
    assert login.is_error() is True
