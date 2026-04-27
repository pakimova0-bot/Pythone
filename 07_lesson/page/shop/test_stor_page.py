from login_page import LoginPage
from product_page import ProductPage
from making_page import MakingPage


def test_form_submission_flow(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    product_page = ProductPage(driver)
    product_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
    product_page.add_item_to_cart("sauce-labs-backpack")
    product_page.add_item_to_cart("sauce-labs-onesie")
    product_page.open_cart()

    making_page = MakingPage(driver)
    making_page.click_checkout_button()
    making_page.input_first_name("Polina")
    making_page.input_last_name("Akimova")
    making_page.input_zip_code("124498")
    making_page.complete_order()
    assert making_page.get_counter()
