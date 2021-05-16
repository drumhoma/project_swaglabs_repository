from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def go_to_checkout(self):
        self.browser.find_element(*CartPageLocators.CHECKOUT_BUTTON).click()
