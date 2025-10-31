from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import json

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
    
    def click_web_element(self, element):
        """Кликнуть по WebElement"""
        element.click()
        return self

    def fill_field(self, element_or_locator, text, timeout = 10):
        """Заполнить поле текстом"""
        element = self.find_element(element_or_locator, timeout)
        element.clear()
        element.send_keys(text)

    def allert_close(self):
        """Получить текст алерта"""
        allert = self.driver.switch_to.alert
        allert.dismiss()
        
    def get_attribute(self, locator, attribute_name):  
        """Получить значение атрибута элемента"""
        element = self.find_element(locator)
        return element.get_attribute(attribute_name)