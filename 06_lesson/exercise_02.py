from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
wait = WebDriverWait(driver, 50)

driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")
print(element)

blue_button = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR, "#updatingButton")))
blue_button.click()

wait.until(EC.text_to_be_present_in_element((
    By.ID, "updatingButton"), "SkyPro"))
print(blue_button.text)

driver.quit()
