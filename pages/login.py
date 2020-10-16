from selenium.webdriver.common.by import By
from pages.inventory import InventoryPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = LoginActions(self.driver, self)

    @property
    def user_name(self):
        return self.driver.find_element(By.ID, "user-name")

    @property
    def password(self):
        return self.driver.find_element(By.ID, "password")

    @property
    def login_button(self):
        return self.driver.find_element(By.ID, "login-button")

    @property
    def login_error(self):
        return self.driver.find_element(By.XPATH, "//h3[@data-test='error']")


class LoginActions:
    def __init__(self, driver, login_page):
        self.driver = driver
        self.login_page = login_page

    def login(self, username, password):
        self.login_page.user_name.type_text(username)
        self.login_page.password.type_text(password)
        self.login_page.login_button.click()
        return InventoryPage(self.driver)
