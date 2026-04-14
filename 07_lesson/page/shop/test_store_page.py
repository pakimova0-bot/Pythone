import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from login_page import LoginPage
from cart_adding import Cart_adding
from making_page import MakingPage 
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = driver = webdriver.Firefox()
    driver.set_page_load_timeout(20)
    yield driver
    driver.quit()

def test_shop():
    login_page = LoginPage
    cart_adding = Cart_adding
    making_page = MakingPage 
    checkout_page = CheckoutPage
             
def test_form_submission_flow(driver):
    login_page = LoginPage(driver)
    login_page = user_field = "standard_user"
    login_page = password_field = "secret_sauce"
    login_page = login_button =  "login-button"

    cart_adding = Cart_adding(driver)
    cart_adding.Sauce_Labs_Backpack_cart = "Sauce_Labs_Backpack_cart"
    cart_adding.Sauce_Labs_Bolt_T_Shirt_cart = "Sauce_Labs_Bolt_T_Shirt_cart"
    cart_adding.Sauce_Labs_Onesie_cart = "Sauce_Labs_Onesie_cart"

    making_page = MakingPage(driver)
    making_page.input_first_name = "Polina"
    making_page.input_last_name  = "Akimova"
    making_page.input_zip_code = "124498"
    making_page.total_cost = "total_cost"

    checkout_page = CheckoutPage(driver)

    text = "Total: $58.29"
    sum_str = text.split(": $")[1]       
    
    
    