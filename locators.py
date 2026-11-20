#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def main():
    options = Options()
    options.add_argument("--window-size=1440,1000")
    driver = webdriver.Chrome(options=options)

    examples = [
        # Основные локаторы
        ("By.ID", By.ID, "user-name"),
        ("By.NAME", By.NAME, "login-button"),
        ("By.CLASS_NAME", By.CLASS_NAME, "inventory_item"),
        ("By.TAG_NAME", By.TAG_NAME, "button"),
        # Эти ссылки доступны в футере каталога после авторизации.
        ("By.LINK_TEXT", By.LINK_TEXT, "Twitter"),
        ("By.PARTIAL_LINK_TEXT", By.PARTIAL_LINK_TEXT, "Face"),

        # XPath: поиск по атрибуту, тексту и частичному совпадению
        ("XPath: по атрибуту", By.XPATH, "//div[@class='inventory_item']"),
        ("XPath: по тексту", By.XPATH, "//div[text()='Sauce Labs Backpack']"),
        ("XPath: contains атрибута", By.XPATH,
         "//button[contains(@data-test,'add-to-cart')]"),
        ("XPath: contains текста", By.XPATH,
         "//div[contains(text(),'Sauce Labs')]"),

        # XPath axes
        ("XPath axis: ancestor", By.XPATH,
         "//div[@class='inventory_item_name']/ancestor::div[@class='inventory_item']"),
        ("XPath axis: descendant", By.XPATH,
         "//div[@class='inventory_item']//descendant::button"),
        ("XPath axis: following", By.XPATH,
         "//div[@class='inventory_item_name']/following::div[@class='inventory_item_price']"),
        ("XPath axis: parent", By.XPATH,
         "//div[@class='inventory_item_name']/parent::*"),
        ("XPath axis: preceding", By.XPATH,
         "//div[@class='inventory_item_price']/preceding::div[@class='inventory_item_name']"),

        # XPath: условие AND
        ("XPath: and", By.XPATH,
         "//input[@name='user-name' and @type='text']"),

        # CSS: классы, комбинации, ID, тег
        ("CSS: .class", By.CSS_SELECTOR, ".inventory_item"),
        ("CSS: .class1.class2", By.CSS_SELECTOR, ".btn.btn_primary"),
        ("CSS: .class1 .class2", By.CSS_SELECTOR, ".inventory_item .inventory_item_name"),
        ("CSS: #id", By.CSS_SELECTOR, "#inventory_container"),
        ("CSS: tagname", By.CSS_SELECTOR, "button"),
        ("CSS: tagname.class", By.CSS_SELECTOR, "button.btn"),

        # CSS: операторы атрибутов из задания
        ("CSS: [attribute=value]", By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']"),
        ("CSS: [attribute~=value]", By.CSS_SELECTOR, "[class~='btn_primary']"),
        ("CSS: [attribute|=value]", By.CSS_SELECTOR, "[data-test|='add-to-cart']"),
        ("CSS: [attribute^=value]", By.CSS_SELECTOR, "[data-test^='add-to-cart']"),
        ("CSS: [attribute$=value]", By.CSS_SELECTOR, "[data-test$='backpack']"),
        ("CSS: [attribute*=value]", By.CSS_SELECTOR, "[data-test*='sauce-labs']"),
    ]

    try:
        driver.get(URL)

        # Вход в систему для доступа к каталогу, товарам и ссылкам футера.
        driver.find_element(By.ID, "user-name").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()

        print("\\nРезультаты проверки локаторов:")
        for title, strategy, locator in examples:
            try:
                elements = driver.find_elements(strategy, locator)
                status = f"найдено: {len(elements)}" if elements else (
                    "не найдено (см. комментарий/проверьте страницу)"
                )
                print(f"{title}: {status} | {locator}")
            except WebDriverException as error:
                print(f"{title}: ошибка локатора: {error.msg}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()