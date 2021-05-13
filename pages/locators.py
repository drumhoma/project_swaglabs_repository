from selenium.webdriver.common.by import By


class LoginPageLocators():
    ICON_LOGO = (By.XPATH, "//div[@class='bot_column']")
    LOGIN_LOGO = (By.XPATH, "//div[@class='login_logo']")

    USERNAME_FIELD = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")

    LOGIN = (By.XPATH, "//div[@class='login_credentials']/text()[1]")  # 1-4
    PASSWORD = (By.XPATH, "//div[@class='login_password']")


class InventoryPageLocator():
    SIDE_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    SELECT_MENU = (By.XPATH, "//select[@class='product_sort_container']")
    SHOP_CART = (By.XPATH, "//a[@class='shopping_cart_link']")
    ADD_TO_CART = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")  # найти все 6
    ITEM_ = (By.XPATH, "//img[@class='inventory_item_img']")  # найти все 6


class CartPageLocator():
    pass


class CheckOutPageLocator():
    pass
