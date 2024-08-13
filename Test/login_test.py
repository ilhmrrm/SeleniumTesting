from selenium import webdriver
import time
import unittest
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        home = HomePage(driver)
        home.click_welcome()
        time.sleep(2)
        home.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        time.sleep(4)
        print("\nSuccessfully completed")

if __name__ == '__main__':
    unittest.main()
