import pytest

from .pages.login_page import LoginPage

link = "https://www.saucedemo.com"


@pytest.mark.users_can_login
class TestLogin:
    def test_should_be_login_attributes(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_logo()
        page.should_be_login_button()


    @pytest.mark.parametrize("password", ["secret_sauce", "no_secret_sauce"])
    @pytest.mark.parametrize("username",
                             ["standard_user", "locked_out_user"])
    def test_standard_user_can_login(self, browser, username, password):
        page = LoginPage(browser, link)
        page.open()
        page.user_login(username)
        page.users_password(password)
        page.login_button_click()
        page.should_be_successful_login()
