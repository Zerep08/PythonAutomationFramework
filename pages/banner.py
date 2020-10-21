from selenium.webdriver.common.by import By
from pages.cart import CartPage


class BannerPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = BannerActions(self.driver, self)

    @property
    def swag_labs_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".app_logo")

    @property
    def cart_icon(self):
        return self.driver.find_element(By.XPATH, "//*[name()='path' and contains(@fill,'currentCol')]")

    @property
    def cart_badge(self):
        return self.driver.find_element(By.CLASS_NAME, "fa-layers-counter.shopping_cart_badge")

    @property
    def peek_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".peek")

    @property
    def left_menu(self):
        return self.driver.find_element(By.XPATH, "//nav[@class='bm-item-list']")

    @property
    def burger_button(self):
        return self.driver.find_element(By.CLASS_NAME, "bm-burger-button")


class BannerActions:
    def __init__(self, driver, banner_page):
        self.driver = driver
        self.banner_page = banner_page

    def click_on_burger_button(self):
        self.banner_page.burger_button.click()

    def get_cart_badge_number(self):
        if self.banner_page.cart_badge.displayed:
            return int(self.banner_page.cart_badge.text)
        else:
            return 0

    def click_on_cart_icon(self):
        self.banner_page.cart_icon.click()
        return CartPage(self.driver)
