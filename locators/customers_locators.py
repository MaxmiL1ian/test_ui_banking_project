from selenium.webdriver.common.by import By

class CustomersLocators: 
    add_customer_button = (By.CSS_SELECTOR, 'button[ng-class = "btnClass1"]')
    customers_button = (By.CSS_SELECTOR, 'button[ng-class = "btnClass3"]')