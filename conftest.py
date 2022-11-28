import json
import pytest

from CONSTANTS import ROOT_DIR
from page_objects.login_page import LoginPage
from utilities.config_parser import ReadConfig
from utilities.configuration import Configuration
from utilities.driver_factory import DriverFactory


@pytest.fixture(scope='session')
def data_store():
    with open(f'{ROOT_DIR}/configurations/configuration.json') as f:
        data = f.read()
        json_to_dict = json.loads(data)

        config = Configuration(**json_to_dict)
        return config


@pytest.fixture()
def create_driver(data_store):
    chrome_driver = DriverFactory.create_driver(ReadConfig.get_browser_id())
    chrome_driver.maximize_window()
    chrome_driver.get(data_store.application_info['base_url'])
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def open_main_page(open_login_page, data_store):
    return open_login_page.login(data_store.user_info['user_name'], data_store.user_info['password'])


@pytest.fixture()
def open_cart_page(open_main_page):
    return open_main_page.open_cart_button()


@pytest.fixture()
def open_shipment_info_page(open_main_page):
    open_main_page.add_to_cart_backpack()
    cart = open_main_page.open_cart_button()
    return cart.click_checkout()


@pytest.fixture()
def open_checkout_overview_page(open_shipment_info_page, data_store):
    page = open_shipment_info_page.set_first_name(data_store.user_info['first_name'])
    page.set_last_name(data_store.user_info['last_name'])
    page.set_postal_code(data_store.user_info['postal_code'])
    return page.click_continue()



