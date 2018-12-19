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

# Wait for page to load
delay = 20 
try:
    FirstName = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'primNavQtip__inner')))
    print("Dashboard loaded sucesfuly.")
except TimeoutException:
    print("Loading took too much time.")

# Go to 'Staff' page and click 'Add Employee'
browser.get('https://itsolutions8.humanity.com/app/staff/list/load/true/')
AddEmployee=browser.find_element_by_id("act_primary")
AddEmployee.click()

# Wait for page to load
delay = 20 
try:
    FirstName = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, '_asf1')))
    print("Add Employees page loaded.")
except TimeoutException:
    print("Loading took too much time.")

# Fill in First Name
FirstName=browser.find_element_by_id("_asf1")
FirstName.send_keys('Cira')

# Fill in Last Name
LastName=browser.find_element_by_id("_asl1")
LastName.send_keys('Tapalaga')

# Fill in Email address
Email=browser.find_element_by_id("_ase1")
Email.send_keys('cira@gmail.com')

# Save new employees data
SaveEmpl=browser.find_element_by_id("_as_save_multiple")
SaveEmpl.click()

# Wait for page to load
delay = 20 
try:
    FirstName = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, '_asf1')))
    print("New Employee saved sucsesfuly.")
except TimeoutException:
    print("Loading took too much time.")


