import time

import pytest

from .pages.login_page import LoginPage

link = "https://www.saucedemo.com/"


@pytest.mark.users_can_login
class TestLogin():
    def test_should_be_login_attributes(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_logo()
        page.should_be_login_button()

    @pytest.mark.debug
    def test_standard_user_can_login(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.standard_user_login()
        page.all_users_password_enter()
        page.do_login()
        page.should_be_successful_login()

    @pytest.mark.debug
    def test_locked_out_user_can_login(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.locked_out_user_login()
        page.all_users_password_enter()
        page.do_login()
        page.should_be_successful_login()

    def test_problem_user_can_login(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.problem_user_login()
        page.all_users_password_enter()
        page.do_login()

    def test_performance_glitch_user_can_login(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.performance_glitch_user_login()
        page.all_users_password_enter()
        page.do_login()

# @pytest.mark.guest_cant_see_product_in_basket
# class TestBasketFromMainPage():
#     def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
#         page = LoginPage(browser, link)
#         page.open()
#         page.go_to_basket_page()
#         basket_page = BasketPage(browser, link)
#         basket_page.should_not_be_product_in_basket()  # в данном методе реализовано два теста
#
