import pytest

from utilities.config_parser import ReadConfig
# login_page


@pytest.mark.smoke
def test_check_logo(open_login_page):
    assert open_login_page.if_login_logo_visible() is True, 'Login logo is not present'


@pytest.mark.regression
def test_if_login_button_present(open_login_page):
    login = open_login_page
    assert login.if_login_visible() is True, 'Login button is not visible'


@pytest.mark.smoke
def test_if_logged_in(open_main_page):
    main_page = open_main_page
    assert main_page.is_cart_visible() is True, 'Not logged in'


@pytest.mark.smoke
@pytest.mark.regression
def test_check_title(create_driver):
    assert create_driver.title == 'Swag Labs'


@pytest.mark.smoke
def test_invalid_login_data(open_login_page):
    login = open_login_page.login('asd', 'asd')
    assert login.is_error() is True


# main_page
@pytest.mark.regression
def test_is_cart_button_present(open_main_page):
    assert open_main_page.is_cart_visible() is True


@pytest.mark.regression
def test_cart_button_leads_to_cart(open_main_page):
    cart = open_main_page.open_cart_button()
    assert cart.is_checkout_visible() is True


@pytest.mark.smoke
def test_product_added_to_cart(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_backpack()
    cart_page = main_page.open_cart_button()
    assert cart_page.is_backpack_added_to_cart() is True


@pytest.mark.regression
def test_is_t_shirt(open_main_page):
    t_shirt = open_main_page.is_t_shirt_visible()
    assert t_shirt is True


@pytest.mark.smoke
def test_is_dropdown_visible(open_main_page):
    dropdown = open_main_page.is_dropdown_visible()
    assert dropdown is True


# cart_page

@pytest.mark.smoke
def test_is_cart_opened(open_cart_page):
    assert open_cart_page.is_checkout_visible() is True, 'Cart is not opened'


@pytest.mark.regression
def test_is_product_added(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_backpack()
    cart_page = main_page.open_cart_button()
    assert cart_page.is_backpack_added_to_cart() is True, ' Backpack is not added to cart'


@pytest.mark.smoke
def test_is_product_deleted(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_backpack()
    cart = main_page.open_cart_button()
    cart.remove_item_from_cart()
    assert cart.is_cart_item_present() is False


@pytest.mark.smoke
def test_continue_shopping(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_backpack()
    main_page.add_to_cart_jacket()
    cart = main_page.open_cart_button()
    cart.click_continue_shopping()
    assert main_page.is_t_shirt_visible() is True


@pytest.mark.smoke
def test_remove_one(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_backpack()
    main_page.add_to_cart_jacket()
    cart = main_page.open_cart_button()
    cart.remove_item_from_cart()
    assert cart.is_cart_item_present() is True


# shipment_info_page

@pytest.mark.regression
def test_is_checkout_opened(open_shipment_info_page):
    assert open_shipment_info_page.is_submit_visible() is True


@pytest.mark.smoke
def test_is_cancel_visible(open_shipment_info_page):
    page = open_shipment_info_page
    assert page.is_submit_visible() is True


@pytest.mark.smoke
def test_continue_with_no_data(open_shipment_info_page):
    page = open_shipment_info_page
    page.click_continue()
    assert page.is_error_visible() is True


@pytest.mark.regression
def test_add_shipping_info(open_shipment_info_page):
    page = open_shipment_info_page
    page.set_first_name(ReadConfig.get_first_name()).set_last_name(ReadConfig.get_last_name())
    page.set_postal_code(ReadConfig.get_postal_code())
    assert page.click_continue().is_finish_visible() is True


@pytest.mark.smoke
def test_click_on_cart(open_shipment_info_page):
    assert open_shipment_info_page.is_robot_visible() is True


# checkout_overview_page

@pytest.mark.smoke
def test_is_checkout_overview_opened(open_checkout_overview_page):
    page = open_checkout_overview_page
    assert page.is_summary_visible() is True


@pytest.mark.regression
def test_is_item_added(open_checkout_overview_page):
    page = open_checkout_overview_page
    assert page.is_inventory_item_visible() is True


@pytest.mark.smoke
def test_is_data_present(open_checkout_overview_page):
    page = open_checkout_overview_page
    assert page.is_total_price_visible() is True


@pytest.mark.smoke
def test_click_finish(open_checkout_overview_page):
    page = open_checkout_overview_page
    page.click_finish()
    assert page.is_compleate_header_visible() is True


@pytest.mark.regression
def test_cancel_button(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_backpack()
    cart = main_page.open_cart_button()
    page = cart.click_checkout().set_first_name(ReadConfig.get_first_name()).set_last_name(ReadConfig.get_last_name())
    page.set_postal_code(ReadConfig.get_postal_code())
    page.click_continue().click_cancel()
    assert main_page.is_t_shirt_visible() is True










