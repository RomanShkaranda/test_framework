import pytest

from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from utilities.config_parser import ReadConfig
from utilities.driver_factory import DriverFactory


@pytest.fixture(scope='session')
def create_driver():
    chrome_driver = DriverFactory.create_driver(ReadConfig.get_browser_id())
    chrome_driver.maximize_window()
    chrome_driver.get(ReadConfig.get_base_url())
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def open_main_page(open_login_page):
    return open_login_page.login(ReadConfig.get_user_name(), ReadConfig.get_password())


@pytest.fixture()
def open_cart_page(open_main_page):
    return open_main_page.open_cart_button()

