from utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __cart_button = (By.XPATH, '//div[@id="shopping_cart_container"]')

    def is_cart_visible(self):
        return self._is_visible(self.__cart_button)
