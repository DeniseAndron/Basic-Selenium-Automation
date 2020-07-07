#open browser with the automatic software selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:/Users/Denisa/Desktop/selenium/chromedriver_win32/chromedriver.exe"


#Filling up a simple form

driver = webdriver.Chrome(path)

driver.get("https://rifinder.com")

sign_up = driver.find_element_by_link_text("REGISTER NOW")
sign_up.click()
time.sleep(3) # wait 3 sec to load

create_new = driver.find_element_by_link_text("Create a new account")
create_new.click()

#find the total number of fields
#input_tag = driver.find_element_by_class_name()
#print(len(input_tag))

first_name = driver.find_element(By.NAME,'first_name').send_keys('rifinderdenisa')
last_name = driver.find_element(By.NAME,'last_name').send_keys('denisarifinder')
user_name = driver.find_element(By.NAME,'user_login').send_keys('rifinderdenisa')
user_email = driver.find_element(By.NAME,'email').send_keys('denn.metal@gmail.com')
user_password = driver.find_element(By.NAME,'password').send_keys('rifinder123')
password_confirmation = driver.find_element(By.NAME,'password_confirmation').send_keys('rifinder123')
time.sleep(1)
button_click = driver.find_element_by_link_text("Register")
button_click.click()