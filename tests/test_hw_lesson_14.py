
import time

from localStoragePy import localStoragePy

# Login Page

def test_check_logo(open_login_page):
    assert open_login_page.if_login_logo_visible() is True, 'Login logo is not present'


def test_if_login_button_present(open_login_page):
    login = open_login_page
    assert login.if_login_visible() is True, 'Login button is not visible'


def test_if_logged_in(open_main_page):
    main_page = open_main_page
    assert main_page.is_cart_visible() is True, 'Not logged in'


def test_check_title(create_driver):
    assert create_driver.title == 'Swag Labs'


def test_invalid_login_data(open_login_page):
    login = open_login_page.login('asd', 'asd')
    assert login.is_error() is True


# Main Page

def test_is_cart_button_present(open_main_page):
    assert open_main_page.is_cart_visible() is True


def test_cart_button_leads_to_cart(open_main_page):
    cart = open_main_page.open_cart_button()
    assert cart.is_checkout_visible() is True


def test_product_added_to_cart(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_backpack()
    cart_page = main_page.open_cart_button()
    assert cart_page.is_backpack_added_to_cart() is True


def test_is_t_shirt(open_main_page):
    t_shirt = open_main_page.is_t_shirt_visible()
    assert t_shirt is True


def test_is_dropdown_visible(open_main_page):
    dropdown = open_main_page.is_dropdown_visible()
    assert dropdown is True


# Cart page

def test_is_cart_opened(open_cart_page):
    assert open_cart_page.is_checkout_visible() is True, 'Cart is not opened'


def test_is_product_added(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_backpack()
    cart_page = main_page.open_cart_button()
    assert cart_page.is_backpack_added_to_cart() is True, ' Backpack is not added to cart'


# test_03 = delete product from cart
def test_is_product_deleted(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_backpack()
    cart = main_page.open_cart_button()
    cart.remove_item_from_cart()
    assert cart.is_cart_item_present() is False

# test_04 = cart icon count
def test_items_in_cart(create_driver, open_main_page):
    open_main_page.add_to_cart_backpack()
    open_main_page.add_to_cart_jacket()
    cockies = create_driver.execute_script('window.localStorage["cart-contents"]')
    assert cockies == [4,0,1]



# test_05 = remove one product from cart










