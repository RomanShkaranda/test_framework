import pytest


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
