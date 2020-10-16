from pages.banner import BannerPage


class InventoryItemPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = InventoryItemActions(self.driver, self)

    @property
    def banner(self):
        return BannerPage(self.driver)


class InventoryItemActions:
    def __init__(self, driver, inventory_item_page):
        self.driver = driver
        self.inventory_item_page = inventory_item_page
