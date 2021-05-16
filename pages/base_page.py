import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import LoginPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def do_screenshot(self):
        self.browser.save_screenshot(f'./screenshots/{time.time()}_screenshot.png')

    def get_text_element(self, how, what):
        # получение текста из атрибута локатора
        return self.browser.find_element(how, what).text

    def should_be_login_logo(self):
        # проверка, что пользователь авторизован
        assert self.is_element_present(*LoginPageLocators.LOGIN_LOGO), "User icon is not presented," \
                                                                       " probably unauthorised user"

    def is_element_present(self, how, what):
        # проверка, что элемент присутствует на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=5):
        # проверка, что элемент не появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=5):
        # проверка, что элемент исчезает со страницы в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
