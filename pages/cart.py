from selenium.webdriver.common.by import By
from re import sub
from decimal import Decimal


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = CartActions(self.driver, self)

    @property
    def cart_items_list(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")


class CartActions:
    def __init__(self, driver, cart_page):
        self.driver = driver
        self.cart_page = cart_page

    def get_cart_items_label(self):
        label_list = []
        for item in self.cart_page.cart_items_list:
            label = item.get_web_element().find_element_by_class_name("inventory_item_name").text
            label_list.append(label)
        return label_list

    def get_cart_items_price(self):
        price_list = []
        for item in self.cart_page.cart_items_list:
            price = item.get_web_element().find_element_by_class_name("inventory_item_price").text
            price = Decimal(sub(r'[^\d.]', '', price))
            price_list.append(price)
        return price_list
