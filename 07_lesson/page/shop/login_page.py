import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __input__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 20)
        self._driver.maximize_window()

        username_field = driver.find_element(By.CSS_SELECTOR, "#user-name")
        password_field = driver.find_element(By.CSS_SELECTOR, "#password")
        login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
        
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        
         
        