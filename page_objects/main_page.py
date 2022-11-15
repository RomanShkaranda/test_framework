from page_objects.cart_page import CartPage
from utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __cart_button = (By.XPATH, '//div[@id="shopping_cart_container"]')
    __add_to_cart_backpack = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')

    def is_cart_visible(self):
        return self._is_visible(self.__cart_button)

    def add_to_cart_backpack(self):
        return self._click(self.__add_to_cart_backpack)

    def open_cart_button(self):
        self._click(self.__cart_button)
        return CartPage(self._driver)


