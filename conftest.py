from contextlib import suppress
import allure
import pytest
from api_collection.data.user_data import User
from page_objects.login_page import LoginPage
from utilities.config_parser import ReadConfig
from utilities.driver_factory import DriverFactory
from utilities.read_json import data_store as d_store


@pytest.fixture(scope='session')
def data_store():
    return d_store()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def create_driver(data_store, request):
    chrome_driver = DriverFactory.create_driver(ReadConfig.get_browser_id())
    chrome_driver.maximize_window()
    chrome_driver.get(data_store.application_info['base_url'])
    yield chrome_driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(chrome_driver.get_screenshot_as_png(), name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
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


@pytest.fixture()
def create_user():
    return User()


