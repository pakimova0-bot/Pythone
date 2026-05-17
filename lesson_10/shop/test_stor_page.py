import allure
from login_page import LoginPage
from product_page import ProductPage
from making_page import MakingPage


@allure.title("Сравнение итоговой суммы заказа с ожидаемой стоимостью")
@allure.feature("Оформление заказа")
@allure.severity("CRITICAL")
@allure.description("""
Этот тест проверяет полный процесс оформления заказа в интернет-магазине:
1. Авторизация стандартного пользователя
2. Добавление товаров в корзину
3. Оформление заказа с вводом персональных данных
4. Проверка корректности итоговой суммы
Ожидаемый результат: Итоговая сумма должна быть равна $58.29
""")
def test_form_submission_flow(driver):
    login_page = LoginPage(driver)
    with allure.step("ввод логина и пароля"):
        login_page.login("standard_user", "secret_sauce")

    product_page = ProductPage(driver)
    with allure.step("ищем товары для покупки, кладем в корзину"):
        product_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
    product_page.add_item_to_cart("sauce-labs-backpack")
    product_page.add_item_to_cart("sauce-labs-onesie")
    with allure.step("кладем товары для покупки"):
        product_page.open_cart()

    making_page = MakingPage(driver)
    with allure.step("переходим в поле для ввода данных для покупки"):
        making_page.click_checkout_button()
        with allure.step("вводим ФИО индекс для оформления заказа"):
            making_page.input_first_name("Polina")
    making_page.input_last_name("Akimova")
    making_page.input_zip_code("124498")
    making_page.complete_order()
    with allure.step(
            "Проверка соответствия итоговой суммы заказа и ожидаемой"):
        as_is = making_page.get_counter()
        assert as_is == 58.29
