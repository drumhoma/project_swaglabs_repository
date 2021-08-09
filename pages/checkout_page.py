from .base_page import BasePage
from .locators import CheckOutPageLocators


class CheckOutPage(BasePage):
    def should_be_login_url(self):
        # проверка, что открыта страница регистрации/авторизации
        url = self.browser.current_url
        assert "login" in url, "'Login' is not contain in URL"

    def checkout_information(self, first_name, last_name, zip_code):
        self.browser.find_element(*CheckOutPageLocators.FIRST_NAME).send_keys(first_name)
        self.browser.find_element(*CheckOutPageLocators.LAST_NAME).send_keys(last_name)
        self.browser.find_element(*CheckOutPageLocators.ZIP_CODE).send_keys(zip_code)

    def go_to_continue(self):
        self.browser.find_element(*CheckOutPageLocators.CONTINUE_BUTTON).click()

    def should_be_successful_checkout(self):
        # проверка, что на странице есть кнопка для логина
        assert self.is_not_element_present(*CheckOutPageLocators.ERROR_MESSAGE), "Checkout ERROR!"

    def go_to_finish(self):
        self.browser.find_element(*CheckOutPageLocators.FINISH_BUTTON).click()

    def go_back_home(self):
        self.browser.find_element(*CheckOutPageLocators.BACK_HOME_BUTTON).click()
