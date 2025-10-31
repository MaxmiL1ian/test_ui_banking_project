import time 
import pytest

class TestBankingProject: 
    def test_add_customer(self, main_page, driver): 
        add_customer_page = main_page.click_add_customer(driver)
        add_customer_page.fill_post_code()
        name = add_customer_page.fill_first_name()
        add_customer_page.fill_last_name() 
        add_customer_page.click_add_customer() 
        add_customer_page.close_allert()
        customers_page = add_customer_page.click_customers(driver)  
        result = customers_page.checking_for_addetion(name) 
        assert result, "Ошибка при создании клиента" 

    def test_sort_descending_first_name(self, main_page, driver): 
        customers_page = main_page.click_customers(driver) 
        customers_page.click_sort_first_name(sort_order="descending")
        result = customers_page.verify_sorting(sort_order="descending") 
        assert result, "Ошибка во время сортировки по убыванию"

    def test_sort_ascending_first_name(self, main_page, driver): 
        customers_page = main_page.click_customers(driver) 
        customers_page.click_sort_first_name(sort_order="ascending")
        result = customers_page.verify_sorting(sort_order="ascending") 
        assert result, "Ошибка во время сортировки по возрастанию"

    def test_delete_user(self, main_page, driver): 
        customers_page = main_page.click_customers(driver)  
        name, index = customers_page.find_closest_to_average_index()
        customers_page.click_delete_by_index(index) 
        result = customers_page.checking_for_deletion(name) 
        assert result, "Ошибка при удалении клиента"
