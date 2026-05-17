from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServer
from webdriver_manager.chrome import ChromeDriverManager
from calc_page import CalculatorPage
import pytest
import allure


@allure.title("Подготовка драйвера браузера и завершения работы драйвера")
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeServer(
        ChromeDriverManager().install()))
    driver.set_page_load_timeout(5)
    yield driver
    driver.quit()


@allure.title("Проверка операций калькулятора: 7+8=15 с задержкой 45 секунд")
@allure.feature("Калькулятор")
@allure.description("""
Тест проверяет основные операции калькулятора,
при этом учитывает задержку вычислений
и ожидает правильный результат.
""")
def test_calculator(driver):
    with allure.step("Открытие страницы калькулятора"):
        calc_page = CalculatorPage(driver)
    calc_page.open()
    with allure.step("Установка задержки 45 секунд"):
        calc_page.enter_delay(driver)
    with allure.step("Нажатие кнопок"):
        calc_page.click_button(driver)
    with allure.step("Ожидание результата"):
        calc_page.get_result(driver)
    with allure.step("Проверяет, что результат на экране калькулятора "
                     "совпадает с ожидаемым результатом"):
        calc_page.get_result(15)
