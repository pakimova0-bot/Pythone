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
    calc_page.delay_fleld()
    calc_page.press_buttons()
    calc_page.check_result()
