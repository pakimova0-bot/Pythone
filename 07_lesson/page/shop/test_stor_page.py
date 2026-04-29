import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from login_page import LoginPage
from product_page import ProductPage
from checkout_page import ShoppingCartPage
from making_page import MakingPage


@pytest.fixture
def open(self, browser):
    self.browser = browser
    browser = webdriver.Firefox()
    self.browser.get("https://www.saucedemo.com/")
    self.wait = WebDriverWait(browser, 20)
    self.browser.maximize_window()


def test_form_submission_flow():
    login_page = LoginPage
    login_page.enter_username
    login_page.enter_password
    login_page.login_button


def add_item_to_cart():
    product_page = ProductPage
    product_page.add_item_to_cart("sauce Labs Backpack")
    product_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    product_page.add_item_to_cart("Sauce Labs Onesie")
    product_page.open_cart()


def search():
    making_page = MakingPage
    making_page.input_first_name("Polina")
    making_page.input_last_name("Akimova")
    making_page.input_zip_code("124498")
    making_page.complete_order()


total_price = MakingPage.get_total_price()
expected_total = 58.29
assert total_price == expected_total
f"Expected total ${expected_total}, but got ${total_price}"


def click_checkout_button():
    checkout_page = ShoppingCartPage()
    checkout_page.click_checkout_button()
