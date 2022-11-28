import pytest


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
