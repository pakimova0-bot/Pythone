import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from login_page import LoginPage
from product_page import ProductPage
from shop_cart_page import ShoppingCartPage
from making_page import MakingPage

@pytest.fixture
def open(self, browser):
    self.browser = browser
    self.browser.get("https://www.saucedemo.com/")
    self.wait = WebDriverWait(browser,20)
    self.browser.maximize_window()  

def test_form_submission_flow():
    browser = webdriver.Firefox()
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

    assert making_page.get_total_amount() == 58.29   
        
def open():       
    shop_cart_page = ShoppingCartPage()
    shop_cart_page.click_checkout_button()
