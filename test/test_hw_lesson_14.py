from utilities.config_parser import ReadConfig


def test_swag_labs_01(open_login_page):
    login_page = open_login_page
    main_page = login_page.login(ReadConfig.get_user_name(), ReadConfig.get_password())

    assert main_page.is_cart_visible() is True

c = 0

