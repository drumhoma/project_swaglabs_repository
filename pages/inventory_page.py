from selenium.webdriver.support.ui import Select

from .base_page import BasePage
from .locators import InventoryPageLocators


class InventoryPage(BasePage):
    def should_be_add_to_basket(self):
        self.should_be_add_to_basket_button()
        self.add_to_basket()
        self.should_be_number_in_basket()

    def should_be_correct_data_in_card(self):
        name = self.get_text_element(*InventoryPageLocators.ITEM_NAME_IN_LINK)
        price = self.get_text_element(*InventoryPageLocators.ITEM_PRICE_IN_LINK)
        self.browser.find_element(*InventoryPageLocators.ITEM_NAME_IN_LINK).click()
        card_name = self.get_text_element(*InventoryPageLocators.ITEM_NAME_IN_CARD)
        card_price = self.get_text_element(*InventoryPageLocators.ITEM_PRICE_IN_CARD)
        assert name == card_name, "The item name in the card is different"
        assert price == card_price, "The item price in the card is different"

    def should_be_back_to_inventory_page(self):
        self.browser.find_element(*InventoryPageLocators.BACK_TO_INVENTORY).click()

    # def should_be_price_in_basket(self):
    #     # проверка, что цена товара в корзине соответствует цене на странице товара
    #     name = self.get_text_element(*InventoryPageLocator.NAME)
    #     basket_name = self.get_text_element(*InventoryPageLocator.BASKET_NAME)
    #     assert name == basket_name, "The item name in the basket is different"

    def should_be_add_to_basket_button(self):
        # проверка, что кнопка добавить в корзину есть на странице
        assert self.is_element_present(*InventoryPageLocators.ADD_TO_CART), "'Add to basket' was not found"

    def add_to_basket(self):
        # добавление товара в корзину
        self.browser.find_element(*InventoryPageLocators.ADD_TO_CART).click()

    def should_be_number_in_basket(self):
        # проверка, что товар добавился в корзину
        assert self.is_element_present(*InventoryPageLocators.NUM_IN_CART), "Item was not added to basket"

    def go_to_basket(self):
        self.browser.find_element(*InventoryPageLocators.SHOP_CART).click()

    def remove_from_page(self):
        self.browser.find_element(*InventoryPageLocators.DEL_FROM_CART).click()
        assert self.is_not_element_present(*InventoryPageLocators.NUM_IN_CART), "Item was not deleted from basket"

    def product_sort(self):
        # выбор сортировки товара
        # подобрать ассерт
        select_menu = Select(self.browser.find_element(*InventoryPageLocators.SELECT_MENU))
        value = self.browser.find_element(*InventoryPageLocators.VALUE_SELECT).text
        select_menu.select_by_visible_text(value)
