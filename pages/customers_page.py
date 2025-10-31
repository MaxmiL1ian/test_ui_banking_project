from .base_page import BasePage  
from locators.customers_locators import CustomersLocators 


class CustomersPage(BasePage):
    def __init__(self, driver):
         super().__init__(driver)

    def click_sort_first_name(self, sort_order): 
        """Метод сортирует по first_name"""

        self.click_element(CustomersLocators.sort_button)  

        if sort_order == "ascending": 
            self.click_element(CustomersLocators.sort_button) 


    def get_text_from_first_names(self):
        """
        Метод возврашает список всех имен

        """
        # Находим все элементы
        elements = self.find_elements(CustomersLocators.first_names)
        
        texts = []
        for element in elements: 
            texts.append(element.text)
        
        return texts
            
    
    def verify_sorting(self, sort_order):
        """
        Проверить сортировку списка текстов
        """
        names = self.get_text_from_first_names()
             
        if sort_order == "ascending":
            return names == sorted(names)
        elif sort_order == "descending":
            return names == sorted(names, reverse=True)
        else:
            return False
        
    def find_closest_to_average_index(self):
        """
        Метод возврашает имя и индекс, которое самое близкое по длине среднему арифметическому длин всех имен
        """
        names = self.get_text_from_first_names()

        # Вычисляем длины всех слов
        lengths = [len(name) for name in names]
        
        # Вычисляем среднее арифметическое
        average_length = sum(lengths) / len(lengths)
        
        # Находим индекс элемента с наиболее близкой длиной
        closest_index = 0
        min_difference = abs(lengths[0] - average_length)
        
        for i in range(1, len(lengths)):
            difference = abs(lengths[i] - average_length)
            if difference < min_difference:
                min_difference = difference
                closest_index = i
        
        return names[closest_index], closest_index
    
    def click_delete_by_index(self, index): 
        """
        Метод выполняет нажатие на кнопку Delete по индексу
        """
        elements = self.find_elements(CustomersLocators.delete_buttons) 
        self.click_web_element(elements[index]) 

    def checking_for_deletion(self, name): 
        """Метод проверяет, что пользователь был удален"""
        try:
            self.fill_field(CustomersLocators.search_input, name) 
            self.find_elements(CustomersLocators.first_names,timeout = 3)
            return False 
        except: 
            return True
        
    def checking_for_addetion(self, name): 
        """
        Метод проверяет, что пользователь был добавлен
        """
        try:
            self.fill_field(CustomersLocators.search_input, name) 
            names = self.get_text_from_first_names() 

            if name in names: 
                return True
            else: 
                return False
        except: 
            return False
