from page_objects.cart_page import CartPage
from utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __cart_button = (By.XPATH, '//div[@id="shopping_cart_container"]')
    __add_to_cart_backpack = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    __add_jacket_to_cart = (By.XPATH, '//button[@name="add-to-cart-sauce-labs-fleece-jacket"]')
    __login_error = (By.XPATH, '//h3[@data-test="error"]')
    __t_shirt = (By.XPATH, '//img[@src="/static/media/bolt-shirt-1200x1500.c0dae290.jpg"]')
    __dropdown = (By.XPATH, '//button[@id="react-burger-menu-btn"]')

    def is_cart_visible(self):
        return self._is_visible(self.__cart_button)

    def add_to_cart_backpack(self):
        return self._click(self.__add_to_cart_backpack)

    def add_to_cart_jacket(self):
        return self._click(self.__add_jacket_to_cart)

    def open_cart_button(self):
        self._click(self.__cart_button)
        return CartPage(self._driver)

    def is_error(self):
        return self._is_visible(self.__login_error)

    def is_t_shirt_visible(self):
        return self._is_visible(self.__t_shirt)

    def is_dropdown_visible(self):
        return self._is_visible(self.__dropdown)


