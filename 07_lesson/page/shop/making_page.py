import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MakingPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com")
        self.wait = WebDriverWait(driver, 20)
        self._driver.maximize_window()

    def making (self):
        self.driver_find_element(By.ID, "#first-name")
        self.first_name = "Polina"
        self.driver.find_element(By.ID, "#last-name")
        self.last_name = "Akimova" 
        self.driver.find_element(By.ID, "#postal-code")
        self.zip_code ="124498"
        self.driver.find_element(By.ID, "#continue").click()

        total_cost = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        total_cost_value = float(total_cost.split("$")[1])

        assert total_cost_value == 58.29
        f"Итоговая сумма должна быть 58.29, но получена {total_cost_value}"
       