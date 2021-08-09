from selenium.webdriver.common.by import By


class MainPageLocators:
    TWITTER_LINK = (By.XPATH, "//li[@class='social_twitter']")
    FB_LINK = (By.XPATH, "//li[@class='social_facebook']")
    LINKEDIN_LINK = (By.XPATH, "//li[@class='social_linkedin']")


class LoginPageLocators:
    LOGIN_LOGO = (By.XPATH, "//div[@class='login_logo']")

    USERNAME_FIELD = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")

    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")


class InventoryPageLocators:
    APP_LOGO = (By.XPATH, "//div[@class='app_logo']")

    SIDE_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    CLOSE_MENU = (By.XPATH, "//button[@id='react-burger-cross-btn']")
    SELECT_MENU = (By.XPATH, "//select[@class='product_sort_container']")
    VALUE_SELECT = (By.XPATH, "//option[@value]")

    SHOP_CART = (By.XPATH, "//a[@class='shopping_cart_link']")
    ADD_TO_CART = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")  # найти все 6
    DEL_FROM_CART = (By.XPATH, "//button[@class='btn btn_secondary btn_small btn_inventory']")  # найти все 6
    NUM_IN_CART = (By.XPATH, "//span[@class='shopping_cart_badge']")

    ITEM_NAME_IN_LINK = (By.XPATH, "//div[@class='inventory_item_name']")  # найти все 6
    ITEM_PRICE_IN_LINK = (By.XPATH, "//div[@class='inventory_item_price']")
    ITEM_NAME_IN_CARD = (By.XPATH, "//div[@class='inventory_details_name large_size']")
    ITEM_PRICE_IN_CARD = (By.XPATH, "//div[@class='inventory_details_price']")
    BACK_TO_INVENTORY = (By.XPATH, "//button[@id='back-to-products']")


class CartPageLocators:
    CHECKOUT_BUTTON = (By.XPATH, "//button[@id='checkout']")
    REMOVE_BUTTON = (By.XPATH, "//button[@class='btn btn_secondary btn_small cart_button']")
    BACK_TO_INVENTORY = (By.XPATH, "//button[@id='continue-shopping']")


class CheckOutPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    ZIP_CODE = (By.XPATH, "//input[@id='postal-code']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id='continue']")
    FINISH_BUTTON = (By.XPATH, "//button[@id='finish']")
    BACK_HOME_BUTTON = (By.XPATH, "//button[@id='back-to-products']")
