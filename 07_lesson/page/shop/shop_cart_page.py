from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartPage:
    def click_checkout_button(self, click_checkout_button):
        self._driver.find_element(EC.element_to_be_clickable((
            By.ID, "checkout"))).checkout_button.click()
