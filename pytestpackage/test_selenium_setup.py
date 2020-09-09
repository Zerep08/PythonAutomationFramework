import pytest
from selenium.webdriver.common.by import By
from base.webdriver_wrapper import Driver

driver = Driver("chrome")


@pytest.fixture()
def setup():
    driver.get_web_driver().maximize_window()
    driver.go_to_url("https://www.google.com/")
    yield
    driver.quit()


def test_search_google_one(setup):
    search_input = driver.find_element(By.NAME, 'q')
    search_input.type_text("Hello this is selenium with python")
    driver.take_screenshot()
