from time import sleep   
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/dynamicid')

sleep(5)
for i in range(3):

    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary").click()

driver.quit()
