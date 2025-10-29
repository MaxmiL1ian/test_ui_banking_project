from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    """Базовый класс для всех страниц"""
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self, url):
        """Открыть указанный URL"""
        self.driver.get(url)
    
    def find_element(self, locator, timeout = 10):
        """Найти элемент с ожиданием"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator, timeout = 10):
        """Найти все элементы с ожиданием"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))
    
    def click_element(self, locator):
        """Кликнуть по элементу"""
        element = self.find_element(locator)
        element.click()
    
    def fill_field(self, element_or_locator, text, timeout = 10):
        """Заполнить поле текстом"""
        element = self.find_element(element_or_locator, timeout)
        element.clear()
        element.send_keys(text)
