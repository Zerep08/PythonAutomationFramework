from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def actions(self):
        return InventoryActions(self.driver)

    @property
    def swag_labs_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".app_logo")

    @property
    def cart_icon(self):
        return self.driver.find_element(By.XPATH, "//*[name()='path' and contains(@fill,'currentCol')]")

    @property
    def peek_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".peek")

    @property
    def sort_drop_down(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".product_sort_container")

    @property
    def product_list(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")

    @property
    def footer(self):
        return self.driver.find_element(By.CLASS_NAME, "footer")

    @property
    def burger_button(self):
        return self.driver.find_element(By.CLASS_NAME, "bm-burger-button")

    @property
    def left_menu(self):
        return self.driver.find_element(By.XPATH, "//nav[@class='bm-item-list']")

    @property
    def cart_badge(self):
        return self.driver.find_element(By.CLASS_NAME, "fa-layers-counter.shopping_cart_badge")


class InventoryActions(InventoryPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_burger_button(self):
        self.burger_button.click()
        return self

    def select_sort_drop_down(self, text):
        drop_down = Select(self.sort_drop_down.get_web_element())
        drop_down.select_by_visible_text(text)
        return self

    def add_random_product_to_cart(self):
        product = random.choice(self.product_list)
        product_name = product.get_web_element().find_element_by_class_name("inventory_item_name").text
        product_price = product.get_web_element().find_element_by_class_name("inventory_item_price").text
        add_to_cart_button = product.get_web_element().find_element_by_class_name("btn_primary.btn_inventory")
        add_to_cart_button.click()
        return product_name, product_price, add_to_cart_button

    def get_cart_badge_number(self):
        if self.cart_badge is None:
            return 0
        else:
            return int(self.cart_badge.text)
