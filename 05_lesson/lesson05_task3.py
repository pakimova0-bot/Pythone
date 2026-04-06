from time import sleep  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

# Найти строку поиска и ввести "Selenium"
search_box = driver.find_element(By.NAME, "button.btn.btn-primary")
search_box.send_keys("Selenium")

# Нажать Enter для выполнения поиска
search_box.send_keys(Keys.RETURN)
search_field = driver.find_element(By.CLASS_SELECTIR, 'input')
search_field.send_keys('123446')

search_field.clear

search_field.send('54321')
driver.quit()

sleep(5)
