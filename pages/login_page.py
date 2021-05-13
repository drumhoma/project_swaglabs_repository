import time

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_logo(self):
        # проверка, что на странице есть логотип
        assert self.is_element_present(*LoginPageLocators.LOGIN_LOGO), "Login logo is not presented"

    def should_be_login_button(self):
        # проверка, что на странице есть кнопка для логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def standard_user_login(self):
        # получить текст из атрибута
        # username = self.browser.find_element(*LoginPageLocators.standard_user)
        username_enter = self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys("standard_user")

    def locked_out_user_login(self):
        username_enter = self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys("locked_out_user")

    def problem_user_login(self):
        username_enter = self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys("problem_user")

    def performance_glitch_user_login(self):
        username_enter = self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(
            "performance_glitch_user")

    def all_users_password_enter(self):
        # password = self.browser.get_text_element(*LoginPageLocators.PASSWORD)
        password_enter = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("secret_sauce")

    def do_login(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def should_be_successful_login(self):
        # проверка, что нет cообщения об ошибке
        text = self.browser.find_element(*LoginPageLocators.ERROR_TEXT)
        assert self.is_not_element_present(*LoginPageLocators.ERROR_MESSAGE), f"{text.text}"
