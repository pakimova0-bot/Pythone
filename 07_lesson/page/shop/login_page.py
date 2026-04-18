from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self._driver = driver

    def enter_username(self, standard_user):
        self._driver.find_element(
            *self.USERNAME_FIELD).send_keys(standard_user)

    def enter_password(self, secret_sauce):
        self._driver.find_element(
            *self.USERNAME_FIELD).send_keys(secret_sauce)

    def login_button(self, login_button):
        self._driver.find_element(
            By.CSS_SELECTOR, "button.login-button").click()
