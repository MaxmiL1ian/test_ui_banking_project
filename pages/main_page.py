from .base_page import BasePage  
from locators.main_locators import MainLocators 
from .customers_page import CustomersPage 
from .add_customer_page import AddCustomerPage
from config import URL 

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def open_page(self):
        """
        Открыть страницу
        """
        self.open(URL)

    def click_add_customer(self, driver): 
        """
        Метод нажимает кнопку добавить клиента
        """
        self.click_element(MainLocators.add_customer_button)
        return AddCustomerPage(driver)
    
    def click_customers(self, driver): 
        """
        Метод нажимает кнопку просмотра клиентов
        """
        self.click_element(MainLocators.customers_button)
        return CustomersPage(driver)
