

class TestBankingProject: 
    def test_add_customer(self, main_page, driver): 
        add_customer_page = main_page.click_add_customer(driver)
        add_customer_page.fill_post_code()
        add_customer_page.fill_first_name()
        add_customer_page.fill_last_name() 
        add_customer_page.click_add_customer()
        message = add_customer_page.get_message_text() 
        assert "Customer added successfully" in message, "Ошибка при создании клиента"