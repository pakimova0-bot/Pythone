from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name):
        selector = f'[data-test="add-to-cart-{item_name}"]'
        self.driver.find_element(By.CSS_SELECTOR, selector).click()

    def open_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
