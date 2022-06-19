import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#####Registration#####
def Registration() :
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")
    driver.implicitly_wait(5)

    My_account_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-50 a")
    My_account_btn.click()
    Reg_mail = driver.find_element(By.ID, "reg_email")
    Reg_mail.send_keys("9520442@gmail.com")
    Reg_pswd = driver.find_element(By.ID, "reg_password")
    Reg_pswd.send_keys("RjhzdsqCkjy")
    time.sleep(3)
    Reg_btn = driver.find_element(By.CSS_SELECTOR, "input[name='register']")
    Reg_btn.click()
    driver.quit()
    exit(0)


#####Login#####
def Login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")
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
    Logout_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[1]/nav/ul/li[6]/a")
    assert EC.presence_of_element_located(Logout_btn)
    if EC.presence_of_element_located(Logout_btn) is not None:
        print("OK!")
    else:
        print("Element is missing!")
    driver.quit()
    exit(0)

#####







