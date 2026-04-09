import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver


def test_slow_calculator(browser):
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    text_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    text_input.clear()
    text_input.send_keys("45")

    buttons = ["7", "+", "8", "="]
    for buttons in buttons:
        xpath = f"//span[text()='{buttons}']"
        browser.find_element(By.XPATH, xpath).click()

    result = WebDriverWait(browser, 46).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"))

    assert (result)

    browser.quit()