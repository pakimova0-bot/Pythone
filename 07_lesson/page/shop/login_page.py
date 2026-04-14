import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 20)
        self._driver.maximize_window()
       
    def login(self, username):
        username_field = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        self.username_field = "standard_user".click()

    def password(self, password):    
        password_field = self.driver.find_element(By.CSS_SELECTOR, "#password")
        self.password_field = "secret_sauce".click()

        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.login-button").click()
        