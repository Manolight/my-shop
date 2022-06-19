import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0, 600);")
Ruby_btn = driver.find_element(By.CSS_SELECTOR, "[title='Selenium Ruby']")
Ruby_btn.click()
driver.execute_script("window.scrollBy(0, 400);")
Reviews_tab = driver.find_element(By.CLASS_NAME, 'reviews_tab')
Reviews_tab.click()
Stars = driver.find_element(By.CLASS_NAME, 'star-5')
Stars.click()
Comments_field = driver.find_element(By.ID, 'comment')
Comments_field.send_keys("Nice book!")
Author_field = driver.find_element(By.ID, "author")
Author_field.send_keys("Vyacheslav")
Email_field = driver.find_element(By.ID, "email")
Email_field.send_keys("9520442@gmail.com")
time.sleep(3)
Submit_btn = driver.find_element(By.ID, "submit")
Submit_btn.click()

time.sleep(3)
driver.quit()
exit(0)