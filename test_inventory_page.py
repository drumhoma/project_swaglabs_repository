import time

import pytest

from .pages.cart_page import CartPage
from .pages.checkout_page import CheckOutPage
from .pages.inventory_page import InventoryPage
from .pages.login_page import LoginPage

link = "https://www.saucedemo.com"


@pytest.mark.parametrize("username",
                         ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"])
@pytest.mark.parametrize("password", ["secret_sauce"])
@pytest.mark.user_add_to_basket
class TestUserAddToBasket:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, username, password):
        page = LoginPage(browser, link)
        page.open()
        page.user_login(username)
        page.users_password(password)
        page.login_button_click()
        page.should_be_successful_login()

    def test_user_can_open_item_card(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_correct_name_in_card()
        page.should_be_back_to_inventory_page()
        page.should_be_correct_price_in_basket()

    @pytest.mark.debug
    @pytest.mark.bug
    def test_user_can_select_product_sort(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.product_sort(0)  # индекс списка сортировки 0 - 3

    def test_user_can_add_to_basket(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_add_to_basket_button()
        page.add_to_basket()
        page.should_be_number_in_basket()
        page.go_to_basket()

    def test_user_can_remove_from_page(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_add_to_basket_button()
        page.add_to_basket()
        page.should_be_number_in_basket()
        page.remove_from_page()
        page.should_not_be_number_in_basket()
        page.go_to_basket()

    def test_user_can_remove_from_basket(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_add_to_basket_button()
        page.add_to_basket()
        page.should_be_number_in_basket()
        page.go_to_basket()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.remove_from_basket()
        cart_page.go_to_inventory()
        page = InventoryPage(browser, browser.current_url)
        page.should_not_be_number_in_basket()

    def test_user_can_go_to_menu(self, browser):
        page = InventoryPage(browser, browser.current_url)
        page.go_to_menu()
        page.close_menu()


# @pytest.mark.parametrize("username",
#                          ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"])
@pytest.mark.parametrize("checkout_information", [
    ("Test", "Test", 123),
    ("Test", "Test", "Test"),
    (123, 123, 123),
    ("Test", "Test", ),
    (" ", " ", " ")
])
@pytest.mark.parametrize("username", [
    "standard_user"
])
@pytest.mark.parametrize("password", [
    "secret_sauce"
])
@pytest.mark.smoke
class TestUserSmoke:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, username, password):
        page = LoginPage(browser, link)
        page.open()
        page.user_login(username)
        page.users_password(password)
        page.login_button_click()

    def test_smoke_from_add_to_buy(self, browser, checkout_information):
        page = InventoryPage(browser, browser.current_url)
        page.should_be_add_to_basket_button()
        time.sleep(1)
        page.product_sort(2)
        time.sleep(1)
        page.add_to_basket()
        time.sleep(1)
        page.product_sort(3)
        time.sleep(1)
        page.add_to_basket()
        time.sleep(1)
        page.should_be_number_in_basket()
        time.sleep(1)
        page.go_to_basket()
        time.sleep(1)
        cart_page = CartPage(browser, browser.current_url)
        cart_page.remove_from_basket()
        time.sleep(1)
        cart_page.go_to_checkout()
        checkout_page = CheckOutPage(browser, browser.current_url)
        checkout_page.checkout_information(checkout_information[0], checkout_information[1], checkout_information[2])
        time.sleep(1)
        checkout_page.go_to_continue()
        time.sleep(1)
        checkout_page.should_be_successful_checkout()
        checkout_page.go_to_finish()
        time.sleep(1)
        checkout_page.go_back_home()
        time.sleep(1)
