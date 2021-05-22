from selenium.webdriver.support.ui import Select

from .base_page import BasePage
from .locators import InventoryPageLocators


class InventoryPage(BasePage):
    def should_be_correct_name_in_card(self):
        # проверка, что наименование товара в корзине соответствует наименованию на странице товара
        name = self.get_text_element(*InventoryPageLocators.ITEM_NAME_IN_LINK)
        self.browser.find_element(*InventoryPageLocators.ITEM_NAME_IN_LINK).click()
        card_name = self.get_text_element(*InventoryPageLocators.ITEM_NAME_IN_CARD)
        assert name == card_name, "The item name in the card is different"

    def should_be_correct_price_in_basket(self):
        # проверка, что цена товара в корзине соответствует цене на странице товара
        price = self.get_text_element(*InventoryPageLocators.ITEM_PRICE_IN_LINK)
        self.browser.find_element(*InventoryPageLocators.ITEM_NAME_IN_LINK).click()
        card_price = self.get_text_element(*InventoryPageLocators.ITEM_PRICE_IN_CARD)
        assert price == card_price, "The item price in the card is different"

    def should_be_back_to_inventory_page(self):
        self.browser.find_element(*InventoryPageLocators.BACK_TO_INVENTORY).click()

    def should_be_add_to_basket_button(self):
        # проверка, что кнопка добавить в корзину есть на странице
        assert self.is_element_present(*InventoryPageLocators.ADD_TO_CART), "'Add to basket' button was not found"

    def add_to_basket(self):
        # добавление товара в корзину
        self.browser.find_element(*InventoryPageLocators.ADD_TO_CART).click()

    def add_all_to_basket(self):
        # добавление всех товаров в корзину
        for i in self.browser.find_elements(*InventoryPageLocators.ADD_TO_CART):
            i.click()

    def should_be_number_in_basket(self):
        # проверка, что на корзине появился индикатор количества товара
        assert self.is_element_present(*InventoryPageLocators.NUM_IN_CART), "Item was not added to basket"

    def should_not_be_number_in_basket(self):
        # проверка, что на корзине отсутствует индикатор количества товара
        assert self.is_not_element_present(*InventoryPageLocators.NUM_IN_CART), "Item was not deleted from basket"

    def go_to_basket(self):
        # переход в корзину
        self.browser.find_element(*InventoryPageLocators.SHOP_CART).click()

    def remove_from_page(self):
        # удаление одного товара из корзины с главной страницы
        self.browser.find_element(*InventoryPageLocators.DEL_FROM_CART).click()

    def remove_all_from_page(self):
        # удаление всех товаров из корзины с главной страницы
        for i in self.browser.find_elements(*InventoryPageLocators.DEL_FROM_CART):
            i.click()

    def product_sort(self, sort):
        # выбор сортировки товара - тест не работает
        before_sort_name = self.get_text_element(*InventoryPageLocators.ITEM_NAME_IN_LINK)
        select_menu = Select(self.browser.find_element(*InventoryPageLocators.SELECT_MENU))
        value_select = []
        for i in self.browser.find_elements(*InventoryPageLocators.VALUE_SELECT):
            value_select.append(i.text)
        select_menu.select_by_visible_text(value_select[sort])
        after_sort_name = self.get_text_element(*InventoryPageLocators.ITEM_NAME_IN_LINK)
        assert before_sort_name != after_sort_name, "Items was not sorted"

    def go_to_menu(self):
        # открыть сайд меню
        self.browser.find_element(*InventoryPageLocators.SIDE_MENU).click()

    def close_menu(self):
        # закрыть сайд меню
        self.browser.find_element(*InventoryPageLocators.CLOSE_MENU).click()
