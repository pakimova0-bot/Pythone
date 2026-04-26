from selenium.webdriver.common.by import By


class LoginPage:
    

    def __init__(self, driver):
        driver = webdriver.Chrome()

    def enter_username(self, driver):
        username_field = driver.find_element(By.CSS_SELECTOR, "#user-name")
        password_field = driver.find_element(By.CSS_SELECTOR, "#password")
        login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()