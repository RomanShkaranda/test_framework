from utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __checkout_button = (By.XPATH, '//button[@id="checkout"]')
    __backpack_element = (By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]')

    def is_checkout_visible(self):
        return self._is_visible(self.__checkout_button)

    def is_backpack_added_to_cart(self):
        return self._is_visible(self.__backpack_element)
