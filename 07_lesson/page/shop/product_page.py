class ProductPage:
    def __init__(self, driver):
        self._driver = driver

    def add_item_to_cart(self, item_name):
        selector = f'[data-test="add-to-cart-{item_name}"]'
        self.wait_for_selector_and_click(selector)

    def open_cart(self):
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)
