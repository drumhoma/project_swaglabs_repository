import time

import pytest

from .pages.cart_page import CartPage
from .pages.checkout_page import CheckOutPage
from .pages.inventory_page import InventoryPage
from .pages.login_page import LoginPage

link = "https://www.saucedemo.com"


# @pytest.mark.parametrize("username",
#                          ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"])
@pytest.mark.parametrize("password", ["secret_sauce"])
@pytest.mark.user_add_to_basket
class TestUserAddToBasket:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser,  password):
        page = LoginPage(browser, link)
        page.open()
        page.user_login("standard_user")
        page.users_password(password)
        page.login_button_click()
        page.should_be_successful_login()

    def test_user_can_open_item_card(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_correct_data_in_card()
        page.should_be_back_to_inventory_page()
        time.sleep(3)

    def test_user_can_select_product_sort(self, browser):
        page = InventoryPage(browser, browser.current_url)
        time.sleep(3)
        page.product_sort()

    def test_user_can_add_to_basket(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_add_to_basket()
        page.go_to_basket()
        time.sleep(3)

    def test_user_can_remove_from_page(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_add_to_basket()
        time.sleep(3)
        page.remove_from_page()
        page.go_to_basket()

    @pytest.mark.debug
    def test_user_can_remove_from_basket(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_add_to_basket()
        time.sleep(1)
        page.go_to_basket()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.remove_from_basket()
        time.sleep(1)
        cart_page.go_to_inventory()


@pytest.mark.parametrize("username", ["performance_glitch_user"])
@pytest.mark.parametrize("password", ["secret_sauce"])
@pytest.mark.user_add_to_basket
class TestUserSmoke:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, username, password):
        page = LoginPage(browser, link)
        page.open()
        page.user_login(username)
        page.users_password(password)
        time.sleep(1)
        page.login_button_click()

    def test_smoke_from_add_to_buy(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_add_to_basket_button()
        page.adds_to_basket()
        page.should_be_number_in_basket()
        time.sleep(1)
        page.go_to_basket()
        cart_page = CartPage(browser, browser.current_url)
        time.sleep(3)
        cart_page.go_to_checkout()
        checkout_page = CheckOutPage(browser, browser.current_url)
        checkout_page.checkout_information("Test", "Test", "123")
        time.sleep(1)
        checkout_page.go_to_continue()
        time.sleep(1)
        checkout_page.go_to_finish()
        time.sleep(1)
        checkout_page.should_be_go_back_home()
