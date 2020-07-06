#open browser with the automatic software selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:/Users/Denisa/Desktop/selenium/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.selenium.dev")

#load using HTML elements

download = driver.find_element_by_link_text("Downloads")
#It will open the download section automatically, always choose the ID if you can
download.click()

#print the search code

#print(driver.page_source)

search = driver.find_element_by_id("gsc-i-id1")

#it will send the text to the search area

search.send_keys("test")

#Returns by pressing enter

search.send_keys(Keys.RETURN)

#Printing the search result

search_result = driver.find_element_by_class_name("gsc-wrapper")
print(search_result.text)

#wait a few seconds then open the search result
try:
    search_result = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gsc-wrapper"))
    )
    print(search_result)
except:
    driver.quit()

driver.quit()

#Navigating through different sections

driver = webdriver.Chrome(path)

driver.get("https://rifinder.com")

courses = driver.find_element_by_link_text("Courses") #finds the link text
courses.click() #clicks the link
time.sleep(6) #waits 6 seconds on the courses page
print(driver.current_url) #print la url
driver.back()#back to the homepage
driver.forward() #back to the courses
driver.close()

driver = webdriver.Chrome(path)

driver.get("https://www.selenium.dev")

search = driver.find_element_by_id("gsc-i-id1")
search.clear() #clear to the search field
time.sleep(2)
search.send_keys('test')
search.send_keys(Keys.RETURN)
driver.close()

#find element by X_Path

driver = webdriver.Chrome(path)

driver.get("https://rifinder.com")

sign_up = driver.find_element_by_xpath('//div[@data-id="5f3e013"]')
sign_up.click()



#is_displayed() && is_enabled() && is_selected()


user_element = driver.find_elements_by_name("user_login-454") #Find the element by the name
print(user_element.is_displayed()) # to see if the field, is displayed
print(user_element.is_enabled()) # to see if the field is enabled

driver.close()

#Implicit Wait    driver.implicitly_wait(3)   it will wait for each line of code
