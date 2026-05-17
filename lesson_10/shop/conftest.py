import pytest
from selenium import webdriver
import allure
import time


@pytest.fixture
@allure.title("Подготовка драйвера браузера")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    yield driver
    driver.quit()
