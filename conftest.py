import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    """Открывает Chrome перед тестом и закрывает его после завершения."""
    options = Options()
    if os.getenv("HEADLESS", "true").lower() in ("1", "true", "yes"):
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()
