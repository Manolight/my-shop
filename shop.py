import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from termcolor import cprint
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()


#####Login#####
def Login():
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    My_account_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-50 a")
    My_account_btn.click()
    Username = driver.find_element(By.ID, "username")
    Username.send_keys("9520442@gmail.com")
    Passwd = driver.find_element(By.ID, "password")
    Passwd.send_keys("RjhzdsqCkjy")
    Login_btn = driver.find_element(By.NAME, "login")
    Login_btn.click()

#####Отображение страницы товара#####
def Product_page_display():
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    Login()
    Shop_btn = driver.find_element(By.ID, "menu-item-40")
    Shop_btn.click()
    HTML5_book = driver.find_element(By.CLASS_NAME, "post-181")
    HTML5_book.click()
    Header = driver.find_element(By.CSS_SELECTOR, "div h1")
    Header_text = Header.text
    assert Header_text == "HTML5 Forms"
    if Header_text == "HTML5 Forms":
        cprint("Passed!", 'green')
    else:
        cprint("ERROR!", 'red')

    driver.quit()


#####Количество товаров в категории#####
def Product_quantity():
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    Login()
    Shop_btn = driver.find_element(By.ID, "menu-item-40")
    Shop_btn.click()
    HTML_cat = driver.find_element(By.CSS_SELECTOR, ".cat-item-19 a")
    HTML_cat.click()
    Pr_field = driver.find_elements(By.CSS_SELECTOR, "div h3")
    Pr_field_quantity = len(Pr_field)
    if Pr_field_quantity == 3:
        cprint("Three products in category! Passed!", "green")
        driver.quit()
    else:
        cprint("ERROR! There are "+ str(Pr_field_quantity)+ " products in category", "red")
        driver.quit()
        exit(1)

#####Сортировка товаров#####
def Sort_products():
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    Login()
    Shop_btn = driver.find_element(By.ID, "menu-item-40")
    Shop_btn.click()
    Sort_by_selector = driver.find_element(By.NAME, "orderby")
    Default_sort = Sort_by_selector.get_attribute("value")
    if Default_sort == "menu_order":
        cprint("Сортировка по умолчанию верная!", "green")
    else:
        cprint("Сортировка по умолчанию неверная!", "red")
    select = Select(Sort_by_selector)
    select.select_by_index(5)
    Sort_by_selector = driver.find_element(By.NAME, "orderby")
    Current_sort = Sort_by_selector.get_attribute("value")
    if Current_sort == "price-desc":
        cprint("Сортировка установлена верно!", "green")
    else:
        cprint("Сортировка установлена неверно!", "red")

#####Отображение, скидка товара#####
def Product_display_discount():
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    Login()
    Shop_btn = driver.find_element(By.ID, "menu-item-40")
    Shop_btn.click()
    Android_guide = driver.find_element(By.CSS_SELECTOR, ".post-169 h3")
    Android_guide.click()
    Old_price = driver.find_element(By.CSS_SELECTOR, ".price del")
    Old_price_value = Old_price.text
    New_price = driver.find_element(By.CSS_SELECTOR, ".price ins")
    New_price_value = New_price.text
    assert Old_price_value == "₹600.00"
    assert New_price_value == "₹450.00"
    Book_preview = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".images .zoom img")))
    Book_preview.click()
    Zoom_close_btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pp_close")))
    Zoom_close_btn.click()

#####Проверка цены в корзине#####
def Cart_price_check():
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    Shop_btn = driver.find_element(By.ID, "menu-item-40")
    Shop_btn.click()
    driver.execute_script("window.scrollBy(0, 300);")
    Add_btn = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
    Add_btn.click()
    time.sleep(3)
    Cart_btn = driver.find_element(By.CLASS_NAME, "wpmenucartli")
    Cart_products_quantity = Cart_btn.text
    Cart_btn_price = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents .amount")
    Cart_btn_price_text = Cart_btn_price.text
    assert Cart_btn_price_text == "₹180.00"
    assert Cart_products_quantity == "1 Item"
    Cart_btn.click()
    time.sleep(3)
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .amount"), "₹180.00")
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .amount"), "₹189.00")


#####Работа в корзине#####
def Cart_operations():
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    Shop_btn = driver.find_element(By.ID, "menu-item-40")
    Shop_btn.click()
    driver.execute_script("window.scrollBy(0, 300);")
    Add_btn_HTML = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
    Add_btn_HTML.click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 600);")
    Add_btn_JS = driver.find_element(By.CSS_SELECTOR, "[data-product_id='180']")
    Add_btn_JS.click()
    Cart_btn = driver.find_element(By.CLASS_NAME, "cartcontents")
    Cart_btn.click()
    time.sleep(3)
    First_remove = driver.find_element(By.CSS_SELECTOR, "tbody :first-child .product-remove .remove")
    First_remove.click()
    Undo_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".woocommerce-message a")))
    Undo_btn.click()
    JS_product_quantity = driver.find_element(By.CSS_SELECTOR, "tbody :nth-child(1) .quantity input")
    JS_product_quantity.clear()
    JS_product_quantity.send_keys(3)
    Update_btn = driver.find_element(By.NAME, "update_cart")
    Update_btn.click()
    JS_product_quantity_text = JS_product_quantity.get_attribute("value")
    assert JS_product_quantity_text == "3"
    time.sleep(3)
    Coupon_btn = driver.find_element(By.NAME, "apply_coupon")
    Coupon_btn.click()
    Coup_error_text = driver.find_element(By.CSS_SELECTOR, ".woocommerce-error li").text
    print(Coup_error_text)
    if Coup_error_text == "Please enter a coupon code.":
        cprint("Passed!", 'green')
    else:
        cprint("Error!", 'red')

######Покупка товара######
def Product_checkout():
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    Shop_btn = driver.find_element(By.ID, "menu-item-40")
    Shop_btn.click()
    driver.execute_script("window.scrollBy(0, 300);")
    Add_btn_HTML = driver.find_element(By.CSS_SELECTOR, "[data-product_id='182']")
    Add_btn_HTML.click()
    time.sleep(3)
    Cart_btn = driver.find_element(By.CLASS_NAME, "wpmenucartli")
    Cart_btn.click()
    Checkout_btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-button")))
    Checkout_btn = driver.find_element(By.CLASS_NAME, "checkout-button")
    Checkout_btn.click()
    First_name_field = wait.until(EC.presence_of_element_located((By.NAME, "billing_first_name")))
    First_name_field.send_keys("Vyacheslav")
    Last_name_field = driver.find_element(By.ID, "billing_last_name")
    Last_name_field.send_keys("Gusak")
    Email_field = driver.find_element(By.ID, "billing_email")
    Email_field.send_keys("9520442@gmail.com")
    Phone_field = driver.find_element(By.ID, "billing_phone")
    Phone_field.send_keys("+79219520442")
    Country_selector = driver.find_element(By.ID, "s2id_billing_country")
    Country_selector.click()
    Country_selector_input = driver.find_element(By.CLASS_NAME, "select2-input")
    Country_selector_input.send_keys("Russia")
    time.sleep(3)
    Country_search_result = driver.find_element(By.CLASS_NAME, "select2-result-label")
    Country_search_result.click()
    Address_field = driver.find_element(By.ID, "billing_address_1")
    Address_field.send_keys("Sedova st. 26")
    City_field = driver.find_element(By.ID, "billing_city")
    City_field.send_keys("St-Petersburg")
    State_field = driver.find_element(By.ID, "billing_state")
    State_field.send_keys("Leningradskaya oblast")
    ZIP_field = driver.find_element(By.ID, "billing_postcode")
    ZIP_field.send_keys("192131")
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(3)
    Payment_method = driver.find_element(By.ID, "payment_method_cheque")
    Payment_method.click()
    Place_order_btn = driver.find_element(By.ID, "place_order")
    Place_order_btn.click()
    Thank_you_message = wait.until(EC.text_to_be_present_in_element
                ((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
    Payment_method_check = wait.until(EC.text_to_be_present_in_element
                ((By.CSS_SELECTOR, "tfoot :nth-child(3) :nth-child(2)"), "Check Payments"))
    Message_text = driver.find_element(By.CLASS_NAME, "woocommerce-thankyou-order-received")
    Message_text_value = Message_text.text
    Payment_method_check_text = driver.find_element(By.CSS_SELECTOR, "tfoot :nth-child(3) :nth-child(2)")
    Payment_method_check_value = Payment_method_check_text.text
    if Message_text_value == "Thank you. Your order has been received." \
            and Payment_method_check_value == "Check Payments":
        cprint("Passed!", 'green')
    else:
        cprint("ERROR!", 'red')



driver.quit()
exit(0)
