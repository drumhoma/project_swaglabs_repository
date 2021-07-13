import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default=None, help="Choose browser: chrome, firefox")
    parser.addoption('--lang', action='store', default="en-gb", help="Choose site language...")
    parser.addoption('--headless', action='store', default='no', help="yes/no")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("lang")
    headless = request.config.getoption("headless")
    print(f"\n\nStart {browser_name} browser for testing...")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument('--start-maximized')  # запуск браузера "во весь экран"
        if headless == "yes":
            options.add_argument('--headless')  # безголовый запуск браузера

        browser = webdriver.Chrome(options=options)
        # browser.maximize_window() # "во весь экран" после запуска браузера
        # browser.set_window_size(1920, 1080) # изменение разрешения после запуска браузера

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference('intl.accept_languages', user_language)
        options.add_argument('--start-maximized')
        if headless == "yes":
            options.add_argument('--headless')

        browser = webdriver.Firefox(options=options)
        # browser.maximize_window()
        # browser.set_window_size(1920, 1080)

    else:
        raise pytest.UsageError("--browser should be chrome or firefox")

    yield browser
    print(f"\nQuit {browser_name} browser...")
    browser.quit()
