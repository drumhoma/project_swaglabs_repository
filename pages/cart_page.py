from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_basket(self):
        # проверка, что в корзине нет товаров
        assert self.is_element_present(*CartPageLocators.EMPTY_BASKET), "Basket is not empty"

    def should_be_text_empty_basket(self):
        # проверка, что есть текст о том, что корзина пуста
        assert self.get_text_element(*CartPageLocators.EMPTY_BASKET) != 0, "No text 'Your basket is empty'"

    def go_to_checkout(self):
        self.browser.find_element(*CartPageLocators.CHECKOUT_BUTTON).click()

    def checkout_information(self, first_name, last_name, zip_code):
        self.browser.find_element(*CartPageLocators.FIRST_NAME).send_keys(first_name)
        self.browser.find_element(*CartPageLocators.LAST_NAME).send_keys(last_name)
        self.browser.find_element(*CartPageLocators.ZIP_CODE).send_keys(zip_code)

    def go_to_continue(self):
        self.browser.find_element(*CartPageLocators.CONTINUE_BUTTON).click()

    def go_to_finish(self):
        self.browser.find_element(*CartPageLocators.FINISH_BUTTON).click()
