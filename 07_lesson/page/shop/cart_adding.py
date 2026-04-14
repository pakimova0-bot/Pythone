import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart_adding:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 20)
        self._driver.maximize_window()

    def cart_adding(self, driver):
        Sauce_Labs_Backpack_cart = driver.find_element(By.ID, "#add-to-cart-sauce-labs-backpack")
        self.Sauce_Labs_Backpack_cart = "Sauce_Labs_Backpack_cart".click()

        Sauce_Labs_Bolt_T_Shirt_cart = driver.find_element(By.ID, "#add-to-cart-sauce-labs-bolt-t-shirt")
        self.Sauce_Labs_Bolt_T_Shirt_cart = "Sauce_Labs_Bolt_T_Shirt_cart".click()

        Sauce_Labs_Onesie_cart = driver.find_element(By.ID, "#add-to-cart-sauce-labs-onesie")
        self.Sauce_Labs_Onesie_cart  = "Sauce_Labs_Onesie_cart ".click()



