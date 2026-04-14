import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com")
        self.wait = WebDriverWait(driver, 20)
        self._driver.maximize_window()

    def click_checkout(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "#checkout")))
        checkout_button.click()
         
      
