import random
from .base_page import BasePage  
from .customers_page import CustomersPage 
from locators.add_customer_locators import AddCustomerLocators

class AddCustomerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.current_post_code = None 
        self.name = None

    def click_customers(self, driver): 
        """
        Метод нажимает кнопку просмотра клиентов
        """
        self.click_element(AddCustomerLocators.customers_button)
        return CustomersPage(driver)
    
    def generate_post_code(self): 
        """
        Генерирует номер из 10 цифр для поля Post Code
        """
        self.current_post_code = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        return self.current_post_code

    def number_to_letter(self, number):
        """
        Преобразует число в букву английского алфавита (0-25 = a-z)
        """
        # Если число больше 25, берем остаток от деления на 26
        normalized_number = number % 26
        return chr(ord('a') + normalized_number) 
    
    def post_code_to_first_name(self):
        """
        Преобразует Post Code в First Name согласно логике
        """
        # Разбиваем Post Code на 5 двузначных чисел
        post_code = self.get_current_post_code()

        two_digit_numbers = []
        for i in range(0, 10, 2):
            two_digit_numbers.append(int(post_code[i:i+2]))
        
        # Преобразуем каждое число в букву
        letters = [self.number_to_letter(num) for num in two_digit_numbers] 
        self.name = ''.join(letters)
        return self.name
    
    def get_current_post_code(self):
        """
        Получить текущий сохраненный post code
        """
        return self.current_post_code
    
    def get_current_name(self): 
        """
        Получить текущее сохраненное имя
        """
        return self.name
    
    def fill_first_name(self):
        """
        Заполнить поле first_name
        """
        first_name = self.post_code_to_first_name()
        self.fill_field(AddCustomerLocators.first_name_input, first_name) 
        return first_name
    
    def fill_last_name(self):
        """
        Заполнить поле last_name
        """
        last_name = self.get_current_name()
        return self.fill_field(AddCustomerLocators.last_name_input, last_name) 
    
    def fill_post_code(self):
        """
        Заполнить поле post_code
        """ 
        post_code = self.generate_post_code()
        return self.fill_field(AddCustomerLocators.post_code_input, post_code)
    
    def click_add_customer(self): 
        """
        Метод нажимает кнопку добавления клиента
        """
        self.click_element(AddCustomerLocators.add_customer_button)

    def close_allert(self):
        """
        Закрыть allert
        """
        return self.allert_close()