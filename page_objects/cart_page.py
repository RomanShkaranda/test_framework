from page_objects.shipment_info_page import ShipmentInfoPage
from utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __checkout_button = (By.XPATH, '//button[@id="checkout"]')
    __backpack_element = (By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]')
    __remove_backpack = (By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')
    __cart_item_element = (By.XPATH, '//div[@class="cart_item"]')
    __cart_number = (By.CSS_SELECTOR, '.shopping_cart_badge')
    __continue_shopping_button = (By.XPATH, '//button[@class="btn btn_secondary back btn_medium"]')

    def is_checkout_visible(self):
        return self._is_visible(self.__checkout_button)

    def is_backpack_added_to_cart(self):
        return self._is_visible(self.__backpack_element)

    def remove_item_from_cart(self):
        return self._click(self.__remove_backpack)

    def is_cart_item_present(self):
        return self._is_visible(self.__cart_item_element)

    def click_continue_shopping(self):
        return self._click(self.__continue_shopping_button)

    def click_checkout(self):
        self._click(self.__checkout_button)
        return ShipmentInfoPage(self._driver)