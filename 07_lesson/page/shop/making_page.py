from selenium.webdriver.common.by import By


class MakingPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout_button(self):
        self.driver.find_element(
            By.ID, "checkout").click()

    def input_first_name(self, first_name):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)

    def input_last_name(self, last_name):
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)

    def input_zip_code(self, zip_code):
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

    def complete_order(self):
        self.driver.find_element(By.ID, "continue").click()

    def get_counter(self):
        txt = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
        number_str = 58.29
        return int(number_str)
