from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_added_product_is_correct_in_cart(browser):
    wait = WebDriverWait(browser, 10)

    # a. Авторизация на SauceDemo.
    browser.get(URL)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(USERNAME)
    browser.find_element(By.ID, "password").send_keys(PASSWORD)
    browser.find_element(By.ID, "login-button").click()

    # b. Выбираем первый товар и сохраняем его название и стоимость.
    product = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    expected_name = product.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text
    expected_price = product.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    # Добавляем выбранный товар в корзину.
    product.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()

    # c. Переходим в корзину.
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_item = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )

    # d. Проверяем название и стоимость через assert.
    actual_name = cart_item.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text
    actual_price = cart_item.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    assert actual_name == expected_name, (
        f"Название товара не совпадает: ожидалось {expected_name!r}, "
        f"получено {actual_name!r}"
    )
    assert actual_price == expected_price, (
        f"Стоимость товара не совпадает: ожидалось {expected_price!r}, "
        f"получено {actual_price!r}"
    )