import pytest
from selenium.webdriver.common.by import By
from base.webdriver_wrapper import Driver
from pages.Login import LoginPage


def test_login_page(setup):
    login_page = LoginPage(setup["Driver"])
    login_page.actions.login(setup["UserName"], setup["Password"])
    assert 1 == 2
