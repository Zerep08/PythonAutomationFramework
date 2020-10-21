from selenium.webdriver.common.by import By
from pages.banner import BannerPage
from pages.inventory import InventoryPage


class InventoryItemPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = InventoryItemActions(self.driver, self)

    @property
    def banner(self):
        return BannerPage(self.driver)

    @property
    def product_title(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_name")

    @property
    def product_image(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_img")

    @property
    def product_description(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_desc")

    @property
    def product_price(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_price")

    @property
    def add_to_cart_button(self):
        return self.driver.find_element(By.CLASS_NAME, "btn_primary.btn_inventory")

    @property
    def remove_button(self):
        return self.driver.find_element(By.CLASS_NAME, "btn_secondary.btn_inventory")

    @property
    def back_button(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_back_button")


class InventoryItemActions:
    def __init__(self, driver, inventory_item_page):
        self.driver = driver
        self.inventory_item_page = inventory_item_page

    def click_on_back_button(self):
        self.inventory_item_page.back_button.click()
        return InventoryPage(self.driver)
