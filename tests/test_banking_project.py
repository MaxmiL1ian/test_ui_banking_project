import allure

class TestBankingProject: 
    @allure.title("Создание нового клиента")
    @allure.description('Тест проверяет возможность создания нового клиента')
    def test_add_customer(self, main_page, driver): 
        with allure.step("Перейти к добавлению нового пользователя"):
            add_customer_page = main_page.click_add_customer(driver)
        with allure.step("Заполнить \"Post code\""):
            add_customer_page.fill_post_code()
        with allure.step("Заполнить \"First name\""):
            name = add_customer_page.fill_first_name()
        with allure.step("Заполнить \"Last name\""):
            add_customer_page.fill_last_name() 
        with allure.step("Нажать кнопку \"Добавить пользователя\""):
            add_customer_page.click_add_customer() 
            add_customer_page.close_allert()
        with allure.step("Проверить, что пользователь добавлен"):
            customers_page = add_customer_page.click_customers(driver)  
            result = customers_page.checking_for_addetion(name) 
            assert result, "Ошибка при создании клиента" 

    @allure.title("Сортировка имен клиентов по убыванию")
    @allure.description('Тест проверяет правильность сортировки имен клиентов по убыванию')
    def test_sort_descending_first_name(self, main_page, driver): 
        with allure.step("Перейти к текущим пользователям"):
            customers_page = main_page.click_customers(driver) 
        with allure.step("Отсортировать по именам в порядке убывания"):
            customers_page.click_sort_first_name(sort_order="descending")
        with allure.step("Проверить правильность сортировки"):
            result = customers_page.verify_sorting(sort_order="descending") 
            assert result, "Ошибка во время сортировки по убыванию"

    @allure.title("Сортировка имен клиентов по возрастанию")
    @allure.description('Тест проверяет правильность сортировки имен клиентов по возрастанию')
    def test_sort_ascending_first_name(self, main_page, driver): 
        with allure.step("Перейти к текущим пользователям"):
            customers_page = main_page.click_customers(driver) 
        with allure.step("Отсортировать по именам в порядке возрастания"):
            customers_page.click_sort_first_name(sort_order="ascending")
        with allure.step("Проверить правильность сортировки"):
            result = customers_page.verify_sorting(sort_order="ascending") 
            assert result, "Ошибка во время сортировки по возрастанию"

    @allure.title("Удаление клиента")
    @allure.description('Тест проверяет возможность удаления клиента')
    def test_delete_user(self, main_page, driver): 
        with allure.step("Перейти к текущим пользователям"):
            customers_page = main_page.click_customers(driver)
        with allure.step("Найти пользователя, у которого длина будет ближе к среднему арифметическому длин имен всех пользователей"):  
            name, index = customers_page.find_closest_to_average_index()
        with allure.step("Удалить выбранного пользователя"):
            customers_page.click_delete_by_index(index) 
        with allure.step("Проверить, что пользователь удален"):
            result = customers_page.checking_for_deletion(name) 
            assert result, "Ошибка при удалении клиента"
