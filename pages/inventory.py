from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.banner import BannerPage
from pages.inventory_item import InventoryItemPage
from re import sub
from decimal import Decimal
import random


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = InventoryActions(self.driver, self)

    @property
    def banner(self):
        return BannerPage(self.driver)

    @property
    def sort_drop_down(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".product_sort_container")

    @property
    def product_list(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")

    @property
    def footer(self):
        return self.driver.find_element(By.CLASS_NAME, "footer")


class InventoryActions:
    def __init__(self, driver, inventory_page):
        self.driver = driver
        self.inventory_page = inventory_page

    def select_sort_drop_down(self, text):
        drop_down = Select(self.inventory_page.sort_drop_down.get_web_element())
        drop_down.select_by_visible_text(text)
        return self

    def add_random_product_to_cart(self):
        product = random.choice(self.inventory_page.product_list)
        product_name = product.get_web_element().find_element_by_class_name("inventory_item_name").text
        product_price = product.get_web_element().find_element_by_class_name("inventory_item_price").text
        add_to_cart_button = product.get_web_element().find_element_by_class_name("btn_primary.btn_inventory")
        add_to_cart_button.click()
        product_price = Decimal(sub(r'[^\d.]', '', product_price))
        return {"name": product_name, "price": product_price, "button": add_to_cart_button}

    def click_on_random_product(self):
        product = random.choice(self.inventory_page.product_list)
        image = product.get_web_element().find_element_by_class_name("inventory_item_img")
        image.click()
        return InventoryItemPage(self.driver)

    def add_random_product_to_cart_and_open_details(self):
        product = random.choice(self.inventory_page.product_list)
        add_to_cart_button = product.get_web_element().find_element_by_class_name("btn_primary.btn_inventory")
        add_to_cart_button.click()
        image = product.get_web_element().find_element_by_class_name("inventory_item_img")
        image.click()
        return InventoryItemPage(self.driver)
