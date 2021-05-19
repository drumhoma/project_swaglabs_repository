from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def go_to_checkout(self):
        self.browser.find_element(*CartPageLocators.CHECKOUT_BUTTON).click()

    def go_to_inventory(self):
        self.browser.find_element(*CartPageLocators.BACK_TO_INVENTORY).click()

    def remove_from_basket(self):
        self.browser.find_element(*CartPageLocators.REMOVE_BUTTON).click()
