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


