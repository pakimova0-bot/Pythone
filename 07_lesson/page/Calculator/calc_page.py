from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-"
            "java/slow-calculator.html")

    def enter_delay(self, driver):
        element = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        element.clear()
        element.send_keys("45")

    def click_button(self, driver):
        driver.find_element(By.XPATH, "//span[text() = '7']").click()
        driver.find_element(By.XPATH, "//span[text() = '+']").click()
        driver.find_element(By.XPATH, "//span[text() = '8']").click()
        driver.find_element(By.XPATH, "//span[text() = '=']").click()

    def get_result(self, driver):
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result.text
        assert result == "15"
