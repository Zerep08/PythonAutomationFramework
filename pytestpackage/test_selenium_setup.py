import pytest
from selenium.webdriver.common.by import By
from base.webdriver_wrapper import Driver
from pages.Login import LoginPage

driver = Driver("chrome")


@pytest.fixture()
def setup():
    driver.get_web_driver().maximize_window()
    driver.go_to_url("https://www.saucedemo.com/")


def test_login_page(setup):
    login_page = LoginPage(driver)
    login_page.actions.login("standard_user", "secret_sauce")
