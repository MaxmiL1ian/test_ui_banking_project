from selenium.webdriver.common.by import By

class AddCustomerLocators: 
    first_name_input = (By.XPATH, '//input[@placeholder = "First Name"]')
    last_name_input = (By.XPATH, '//input[@placeholder = "Last Name"]')
    post_code_input = (By.XPATH, '//input[@placeholder = "Post Code"]') 
    add_customer_button = (By.XPATH, '//button[@type = "submit"]') 
    customers_button = (By.CSS_SELECTOR, 'button[ng-class = "btnClass3"]')