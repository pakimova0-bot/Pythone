import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __input__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 20)
        self._driver.maximize_window()

    def search(self):
        self._driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys()
        self._driver.find_element(By.CSS_SELECTOR, "#button[type=submit]").click() 

        self.driver.find_element(By.ID, "Sauce Labs Backpack").send_keys() 
        self.driver.find_element(By.ID, "Sauce Labs Bolt T-Shirt").send_keys() 
        self.driver.find_element(By.ID, "Sauce Labs Onesie").send_keys() 

        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").cart_link.click()  