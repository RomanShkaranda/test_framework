from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage


class CheckoutOverview(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __finish_button = (By.CSS_SELECTOR, '#finish')
    __summary_info = (By.CSS_SELECTOR, '.summary_info_label')
    __inventory_item = (By.CSS_SELECTOR, '.inventory_item_name')
    __total_price = (By.CSS_SELECTOR, '.summary_total_label')
    __complete_header = (By.CSS_SELECTOR, '.complete-header')
    __cancel_button = (By.CSS_SELECTOR, '#cancel')

    def is_finish_visible(self):
        return self._is_visible(self.__finish_button)

    def is_summary_visible(self):
        return self._is_visible(self.__summary_info)

    def is_inventory_item_visible(self):
        return self._is_visible(self.__inventory_item)

    def is_total_price_visible(self):
        return self._is_visible(self.__total_price)

    def click_finish(self):
        return self._click(self.__finish_button)

    def is_compleate_header_visible(self):
        return self._is_visible(self.__complete_header)

    def click_cancel(self):
        return self._click(self.__cancel_button)


