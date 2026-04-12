import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from login_page import LoginPage
from main_page import MainPage
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
    main_page = MainPage
    making_page = MakingPage
    checkout_page = CheckoutPage
             
def test_form_submission_flow(driver):
    login_page = LoginPage()
    login_page.username_field.send_keys("standard_user")
    login_page.password_field.send_keys("secret_sauce")
    login_page.click_login_button()

    main_page = MainPage(driver)
    main_page. add_goosd()
    main_page.go_to_cart

    making_page = MakingPage(driver)
    making_page.push_buttons()
    making_page.add_item_to_cart("sauce-labs-backpack")
    making_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
    making_page.add_item_to_cart("sauce-labs-onesie")
    making_page.navigate_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_from()
    checkout_page.input_first_name("Акимова")
    checkout_page.input_last_name("Полина")
    checkout_page.input_zip_code("124498")
    checkout_page.complete_order()

    assert checkout_page.get_total_cost_value () == 58.29
        
    
    
    