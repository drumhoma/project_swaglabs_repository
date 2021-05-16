from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_logo(self):
        # проверка, что на странице есть логотип
        assert self.is_element_present(*LoginPageLocators.LOGIN_LOGO), "Login logo is not presented"

    def should_be_login_button(self):
        # проверка, что на странице есть кнопка для логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def user_login(self, username):
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(username)

    def users_password(self, password):
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    def login_button_click(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def should_be_successful_login(self):
        # проверка, что на странице есть кнопка для логина
        assert self.is_not_element_present(*LoginPageLocators.ERROR_MESSAGE), "Autorizaion ERROR!"
