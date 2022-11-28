import pytest

from page_objects.login_page import LoginPage
from utilities.config_parser import ReadConfig
from utilities.driver_factory import DriverFactory


@pytest.fixture()
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


@pytest.fixture()
def open_shipment_info_page(open_main_page):
    open_main_page.add_to_cart_backpack()
    cart = open_main_page.open_cart_button()
    return cart.click_checkout()


@pytest.fixture()
def open_checkout_overview_page(open_shipment_info_page):
    page = open_shipment_info_page.set_first_name(ReadConfig.get_first_name()).set_last_name(ReadConfig.get_last_name())
    page.set_postal_code(ReadConfig.get_postal_code())
    return page.click_continue()



