import time

import pytest

from .pages.login_page import LoginPage
from .pages.inventory_page import InventoryPage
from .pages.cart_page import CartPage

link = "https://www.saucedemo.com"


@pytest.mark.user_add_to_basket
class TestUserAddToBasket():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.do_login()

    def test_standard_user_can_open_item_card(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_correct_data_in_card()
        page.should_be_back_to_inventory_page()
        time.sleep(3)

    def test_standard_user_can_select_product_sort(self, browser):
        page = InventoryPage(browser, browser.current_url)
        time.sleep(3)
        page.product_sort()

    def test_standard_user_can_add_to_basket(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_add_to_basket()
        page.go_to_basket()
        time.sleep(3)

    def test_standard_user_can_remove_from_page(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_add_to_basket()
        time.sleep(3)
        page.remove_from_page()
        page.go_to_basket()


@pytest.mark.debug
@pytest.mark.user_add_to_basket
class TestUserSmoke():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.do_login()

    def test_smoke_from_add_to_buy(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_add_to_basket()
        page.go_to_basket()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.go_to_checkout()
        cart_page.checkout_information("Test", "Test", "123")
        cart_page.go_to_continue()
        cart_page.go_to_finish()
        time.sleep(3)
