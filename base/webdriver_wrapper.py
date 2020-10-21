from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.webelement_wrapper import Element
from base.Browser import BrowserDriverFactory
from Screenshot import Screenshot_Clipping
from datetime import datetime
from selenium.common.exceptions import TimeoutException
import os


class Driver:
    def __init__(self, browser_driver):
        self.__web_driver = BrowserDriverFactory.create_driver(browser_driver)
        self.__wait = WebDriverWait(self.__web_driver, 6)

    def find_element(self, by, locator):
        try:
            element = self.__wait.until(ec.presence_of_element_located((by, locator)))
            return Element(self.__web_driver, element, by, locator)
        except TimeoutException:
            print(f'Element {locator} not found after 6 seconds')
            return Element(self.__web_driver, None, by, locator)

    def find_elements(self, by, locator):
        try:
            elements = []
            results = self.__wait.until(ec.presence_of_all_elements_located((by, locator)))
            for element in results:
                elements.append(Element(self.__web_driver, element, by, locator))
            return elements
        except TimeoutException:
            print(f'Element {locator} not found after 6 seconds')
            return []

    def go_to_url(self, url):
        self.__web_driver.get(url)

    def quit(self):
        self.__web_driver.quit()

    def maximise_window(self):
        self.__web_driver.maximize_window()

    def get_web_driver(self):
        return self.__web_driver

    def take_screenshot(self, image_name):
        path = self.__get_screenshots_folder_path()
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        ss_obj = Screenshot_Clipping.Screenshot()
        ss_obj.full_Screenshot(self.__web_driver, save_path=path, image_name=f"{image_name}_{timestamp}.png")

    @staticmethod
    def __get_screenshots_folder_path():
        full_path = os.path.abspath("")
        end_index = full_path.find("PythomationFW")
        root_path = full_path[:end_index]
        return "{0}PythomationFW/screenshots".format(root_path)
