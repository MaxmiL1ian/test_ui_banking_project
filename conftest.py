import pytest
from selenium import webdriver

@pytest.fixture(scope = 'session',autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager' 
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()