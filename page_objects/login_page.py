from selenium.webdriver.common.by import By
from page_objects.main_page import MainPage
from utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(self.__driver)

    __user_name = (By.XPATH, '//input[@id="user-name"]')
    __password = (By.XPATH, '//input[@id="password"]')
    __login_button = (By.XPATH, '//input[@id="login-button"]')
    __login_logo = (By.XPATH, '//div[@class="login_logo"]')

    def set_user_name(self, user_name):
        self._send_keys(self.__user_name, user_name)
        return self

    def set_password(self, password):
        self._send_keys(self.__password, password)
        return self

    def click_login(self):
        self._click(self.__login_button)

    def login(self, user_name, password):
        self.set_user_name(user_name).set_password(password).click_login()
        return MainPage(self.__driver)

    def if_login_visible(self):
        return self._is_visible(self.__login_button)

    def if_login_logo_visible(self):
        return self._is_visible(self.__login_logo)


