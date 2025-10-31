import pytest
from selenium import webdriver 
from pages.main_page import MainPage

@pytest.fixture(scope = 'function',autouse=True)
def driver():
    driver = webdriver.Chrome()
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