from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowserDriverFactory:
    @staticmethod
    def create_driver(browser_type):
        if browser_type == "chrome":
            return webdriver.Chrome(ChromeDriverManager().install())
        elif browser_type == "firefox":
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            raise NotImplemented
