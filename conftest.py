import pytest
from selenium import webdriver 
from pages.main_page import MainPage

@pytest.fixture(scope = 'session',autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    #options.page_load_strategy = 'eager'  # Не ждать полной загрузки всех ресурсов

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(90)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()

@pytest.fixture(scope = 'function')
def main_page(driver):
    """Фикстура для открытия страницы"""
    page = MainPage(driver)
    page.open_page()  # Открываем страницу
    return page