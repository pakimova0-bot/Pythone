import pytest
from selenium import webdriver
import allure


@allure.step("Настройка, обращение к драйверу браузера Firefox")
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
