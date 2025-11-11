from selenium.webdriver.common.by import By

class CustomersLocators: 
    state_sort = (By.CSS_SELECTOR, 'a[ng-click="sortType = \'fName\'; sortReverse = !sortReverse"]>.fa.fa-caret-up') 
    sort_button = (By.CSS_SELECTOR, 'a[ng-click = "sortType = \'fName\'; sortReverse = !sortReverse"]') 
    first_names = (By.CSS_SELECTOR,'tr.ng-scope>:nth-child(1)')
    delete_buttons = (By.XPATH, '//button[text()="Delete"]')
    search_input = (By.CSS_SELECTOR,'input[placeholder="Search Customer"]')