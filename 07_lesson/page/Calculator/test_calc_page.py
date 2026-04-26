from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServer
from webdriver_manager.chrome import ChromeDriverManager
from calc_page import CalculatorPage
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeServer(
        ChromeDriverManager().install()))
    driver.set_page_load_timeout(5)
    yield driver
    driver.quit()


def test_calculator(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open()
    calc_page.enter_delay(driver)
    calc_page.click_button(driver)
    calc_page.get_result(driver)
    calc_page.get_result(driver)
