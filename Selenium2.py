from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Go to Humanity webpage
browser = webdriver.Firefox()
browser.get('https://itsolutions8.humanity.com/app/')

# Enter username
username=browser.find_element_by_id("email")
username.send_keys('irinelko@gmail.com')

# Enter password
password=browser.find_element_by_id("password")
password.send_keys('Humanity')
password.submit()

# Wait for Dashboard to load
delay = 20 
try:
    FirstName = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'primNavQtip__inner')))
    print("Dashboard loaded sucesfuly.")
except TimeoutException:
    print("Loading took too much time.")

# Go to 'Time Clock' page
browser.get('https://itsolutions8.humanity.com/app/timeclock/')

# Wait for 'Time Clock' page to load
try:
    FirstName = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'tc_tl_ci')))
    print("'Time Clock' loaded sucesfuly.")
except TimeoutException:
    print("Loading took too much time.")

# Click 'Clock in'    
ClockIn=browser.find_element_by_id("tc_tl_ci")
ClockIn.click()

# Wait to be Clocked in
try:
    FirstName = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'tc_tl_co')))
    print("Clocked in sucsesfuly.")
except TimeoutException:
    print("Loading took too much time.")

# Click 'Clock out'
ClockOut=browser.find_element_by_id("tc_tl_co")
ClockOut.click()

# Wait to be Clocked out
try:
    FirstName = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'tc_tl_ci')))
    print("Clocked out sucsesfuly.")
except TimeoutException:
    print("Loading took too much time.")

browser.quit()


