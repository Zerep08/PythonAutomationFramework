from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.support.ui import WebDriverWait


class Element:
    def __init__(self, driver, web_element, by, locator):
        self.__driver = driver
        self.__web_element = web_element
        self.__by = by
        self.__locator = locator

    @property
    def text(self):
        return self.__web_element.text

    @property
    def enabled(self):
        return self.__web_element.is_enabled()

    @property
    def displayed(self):
        return self.__web_element.is_displayed()

    def click(self):
        self.__wait_to_be_clickable()
        self.__web_element.click()

    def get_attribute(self, name):
        return self.__web_element.get_attribute(name)

    def type_text(self, text):
        self.__web_element.send_keys(text)

    def clear(self):
        self.__web_element.clear()

    def __wait_to_be_clickable(self):
        wait = WebDriverWait(self.__driver, 6)
        wait.until(condition.element_to_be_clickable((self.__by, self.__locator)))

    def get_web_element(self):
        return self.__web_element

    def get_locator(self):
        return self.__locator
