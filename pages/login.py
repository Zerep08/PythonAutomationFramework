from selenium.webdriver.common.by import By
from pages.inventory import InventoryActions
from assertpy import assert_that


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

    def error_displayed_for_invalid_login(self):
        assert_that(self.login_error.displayed).is_equal_to(True)
        assert_that(self.login_error.text).is_equal_to("Epic sadface: Sorry, this user has been locked out.")
