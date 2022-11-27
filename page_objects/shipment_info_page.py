from page_objects.checkout_overview_page import CheckoutOverview
from utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class ShipmentInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __submit_button = (By.XPATH, '//input[@class="submit-button btn btn_primary cart_button btn_action"]')
    __cancel_button = (By.XPATH, '//button[@class="btn btn_secondary back btn_medium cart_cancel_link"]')
    __error = (By.XPATH, '//div[@class="error-message-container error"]')
    __first_name = (By.CSS_SELECTOR, '#first-name')
    __last_name= (By.CSS_SELECTOR, '#last-name')
    __postal_code= (By.CSS_SELECTOR, '#postal-code')
    __cart_button = (By.XPATH, '//div[@id="shopping_cart_container"]')
    __robot = (By.XPATH, '//img[@class="footer_robot"]')

    def is_submit_visible(self):
        return self._is_visible(self.__submit_button)

    def is_cancel_button_clickable(self):
        return self._is_visible(self.__cancel_button)

    def click_continue(self):
        self._click(self.__submit_button)
        return CheckoutOverview(self._driver)

    def is_error_visible(self):
        return self._is_visible(self.__error)

    def set_first_name(self, first_name):
        self._send_keys(self.__first_name, first_name)
        return self

    def set_last_name(self, last_name):
        self._send_keys(self.__last_name, last_name)
        return self

    def set_postal_code(self, postal_code):
        self._send_keys(self.__postal_code, postal_code)
        return self

    def is_robot_visible(self):
        return self._is_visible(self.__robot)


