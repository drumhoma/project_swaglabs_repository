import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

link = "https://www.saucedemo.com"


@pytest.mark.users_can_login
class TestLinks:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.user_login("standard_user")
        page.users_password("secret_sauce")
        page.login_button_click()
        page.should_be_successful_login()

    @pytest.mark.debug
    def test_should_be_twitter_link(self, browser):
        page = MainPage(browser, browser.current_url)
        page.open()
        page.should_be_twitter_link()
        page.link_click()

    def test_should_be_fb_link(self, browser):
        page = MainPage(browser, browser.current_url)
        page.open()
        page.should_be_fb_link()
        page.element_is_clickable()

    def test_should_be_linkedin_link(self, browser):
        page = MainPage(browser, browser.current_url)
        page.open()
        page.should_be_linkedin_link()
        page.element_is_clickable()
