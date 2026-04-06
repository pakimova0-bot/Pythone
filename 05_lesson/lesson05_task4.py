from time import sleep  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

un = "input[name='username']"
push_login = driver.find_element(By.CSS_SELECTOR, un)
push_login.send_keys("tomsmith")

pw = "input[id='password']"
push_pass = driver.find_element(By.CSS_SELECTOR, pw)
push_pass.send_keys("SuperSecretPassword!")

sleep(10)

log = "button.radius"
push_login = driver.find_element(By.CSS_SELECTOR, log)
log.click()

success_massage = drive.find_element(By.CSS_SELECTOR, "div.flash.success")
print(success_massage.text)

sleep(10)
