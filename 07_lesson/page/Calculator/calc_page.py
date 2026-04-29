from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
    "slow-calculator.html")

    def delay_fleld(self):
        element = self.driver.find_element(
            By.CSS_SELECTOR, "#delay")
        element.clear()
        element.send_keys("45")

    def press_buttons(self):
        buttons = ["7", "+", "8", "="]
        for buttons in buttons:
            xparh = f"//span[text()='{buttons}']"
            self.driver.find_element(By.XPATH, xparh).click()
            buttons = ["7", "+", "8", "="]

    def expectation(self):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15"))

    def get_result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result.text
