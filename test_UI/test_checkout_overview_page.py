import pytest


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
def test_cancel_button(open_main_page, data_store):
    main_page = open_main_page
    main_page.add_to_cart_backpack()
    cart = main_page.open_cart_button()
    page = cart.click_checkout()
    page.set_first_name(data_store.user_info['first_name'])
    page.set_last_name(data_store.user_info['last_name'])
    page.set_postal_code(data_store.user_info['postal_code'])
    page.click_continue().click_cancel()
    assert main_page.is_t_shirt_visible() is True
