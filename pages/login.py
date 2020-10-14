from selenium.webdriver.common.by import By
from pages.inventory import InventoryActions



class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def actions(self):
        return LoginActions(self.driver)

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


class LoginActions(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self, username, password):
        self.user_name.type_text(username)
        self.password.type_text(password)
        self.login_button.click()
        return InventoryActions(self.driver)
