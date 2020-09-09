from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest:

    def test_valid_login(self):
        base_url = "https://letskodeit.com/"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        login_link = driver.find_element_by_xpath("//div[@class='ast-button']")
        login_link.click()

        email = driver.find_element_by_id("email")
        email.send_keys("test@email.com")

        password = driver.find_element_by_id("password")
        password.send_keys("abcabc")

        login_button = driver.find_element_by_xpath("//input[@class='btn btn-default btn-block btn-md dynamic-button']")
        login_button.click()

        avatar = driver.find_element_by_css_selector("div.dropdown")
        if avatar is not None:
            print("Login Successfully")


wea = LoginTest()
wea.test_valid_login()
