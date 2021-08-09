from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_twitter_link(self):
        # проверка, что на странице есть логотип
        assert self.is_element_present(*MainPageLocators.TWITTER_LINK), "Twitter link is not presented"

    def should_be_fb_link(self):
        # проверка, что на странице есть кнопка для логина
        assert self.is_element_present(*MainPageLocators.FB_LINK), "FB link is not presented"

    def should_be_linkedin_link(self):
        # проверка, что на странице есть логотип
        assert self.is_element_present(*MainPageLocators.LINKEDIN_LINK), "Linkedin_link is not presented"

    def link_click(self):
        self.browser.find_element(*MainPageLocators.TWITTER_LINK).click()

    # def should_be_successful_login(self):
    #    # проверка, что на странице есть кнопка для логина
    #    try:
    #        text_error = self.get_text_element(*LoginPageLocators.ERROR_MESSAGE)
    #        assert text_error == "Epic sadface: Sorry, this user has been locked out.", "Authorization ERROR!"
    #    except NoSuchElementException:
    #        return True
    #    return False
