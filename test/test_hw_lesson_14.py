from utilities.config_parser import ReadConfig


def test_login_01(open_login_page):
    login_page = open_login_page
    main_page = login_page.login(ReadConfig.get_user_name(), ReadConfig.get_password())
    assert main_page.is_cart_visible() is True


def test_is_cart_opened_03(open_login_page):
    cart = open_login_page.login(ReadConfig.get_user_name(), ReadConfig.get_password()).open_cart_button()
    assert cart.is_checkout_visible() is True


def test_adding_to_cart_03(open_login_page):
    main_page = open_login_page.login(ReadConfig.get_user_name(), ReadConfig.get_password())
    main_page.add_to_cart_backpack()
    cart = main_page.open_cart_button()
    assert cart.is_backpack_added_to_cart() is True
