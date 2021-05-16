from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_LOGO = (By.XPATH, "//div[@class='login_logo']")

    USERNAME_FIELD = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")

    STANDARD_USER = (By.XPATH, "//div[@id='login_credentials']/text()")
    LOCKED_OUT_USER = (By.XPATH, "//div[@class='login_credentials']/text()[2]")
    PROBLEM_USER = (By.XPATH, "//div[@class='login_credentials']/text()[3]")
    PERFOMANCE_GLITCH_USER = (By.XPATH, "//div[@class='login_credentials']/text()[4]")
    PASSWORD = (By.XPATH, "//div[@class='login_password']")

    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")


class InventoryPageLocators:
    APP_LOGO = (By.XPATH, "//div[@class='app_logo']")

    SIDE_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    SELECT_MENU = (By.XPATH, "//select[@class='product_sort_container']")
    VALUE_SELECT = (By.XPATH, "//option[@value][4]")

    ITEM_NAME_IN_LINK = (By.XPATH, "//div[@class='inventory_item_name']")  # найти все 6
    ITEM_NAME_IN_CARD = (By.XPATH, "//div[@class='inventory_details_name large_size']")
    ITEM_PRICE_IN_LINK = (By.XPATH, "//div[@class='inventory_item_price']")
    ITEM_PRICE_IN_CARD = (By.XPATH, "//div[@class='inventory_details_price']")
    BACK_TO_INVENTORY = (By.XPATH, "//button[@id='back-to-products']")

    SHOP_CART = (By.XPATH, "//a[@class='shopping_cart_link']")
    ADD_TO_CART = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")  # найти все 6
    DEL_FROM_CART = (By.XPATH, "//button[@class='btn btn_secondary btn_small btn_inventory']")  # найти все 6
    NUM_IN_CART = (By.XPATH, "//span[@class='shopping_cart_badge']")


class CartPageLocators:
    CHECKOUT_BUTTON = (By.XPATH, "//button[@id='checkout']")


class CheckOutPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    ZIP_CODE = (By.XPATH, "//input[@id='postal-code']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id='continue']")
    FINISH_BUTTON = (By.XPATH, "//button[@id='finish']")
    BACK_HOME_BUTTON = (By.XPATH, "//button[@id='back-to-products']")
