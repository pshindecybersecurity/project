from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SoftwareProject.Pages.loginpage  import LoginPage
from SoftwareProject.Pages.homepage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Safari()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        # homepage = HomePage(driver)
        # homepage.click_welcome()
        # homepage.click_logout()

        time.sleep(5)

    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/pravinshinde/Documents/Project/SoftwareProject/reports'))