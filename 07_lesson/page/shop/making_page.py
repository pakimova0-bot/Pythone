from selenium.webdriver.common.by import By


class MakingPage:
    def __init__(self, driver):
        self._driver = driver
        
    def input_first_name(self, first_name):
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)

    def input_last_name(self, last_name):
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)

    def input_zip_code(self, zip_code):
        self._driver.find_element(By.ID, "postal-code").send_keys(zip_code)

    def complete_order(self, complete_order):
        self._driver.find_element(By.ID, "continue").click(complete_order)

    def total(self, total):
        self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
    text = "Total: $58.29"
    sum_str = text.split(": $")[1]
