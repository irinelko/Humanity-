import unittest
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class FirefoxTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('https://itsolutions8.humanity.com/app/')
        self.browser.find_element_by_id("email").send_keys('irinelko@gmail.com')
        self.browser.find_element_by_id("password").send_keys('Humanity')
        self.browser.find_element_by_id("password").submit()
        try:
            logedIn = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'primNavQtip__inner')))
        except TimeoutException:
            print("Browser not responding.")
        
    def test_Clock_IN_OUT(self):
        TestPassed=True
        self.browser.get('https://itsolutions8.humanity.com/app/timeclock/')
        try:
            ClockIn = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.ID, 'tc_tl_ci')))
        except TimeoutException:
            TestPassed=False
  
        try:
            self.browser.find_element_by_id("tc_tl_ci").click()
        except TimeoutException:
            TestPassed=False

        try:
            FirstName = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.ID, 'tc_tl_co')))
        except TimeoutException:
              TestPassed=False

        self.browser.find_element_by_id("tc_tl_co").click()

        try:
            FirstName = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, 'tc_tl_ci')))
        except TimeoutException:
            TestPassed=False

        self.assertTrue(TestPassed)


    def test_Add_Employee(self):

        OK=True
        self.browser.get('https://itsolutions8.humanity.com/app/staff/list/load/true/')
        try:
            FirstName = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'staff-employee')))
            Names = [el.text for el in self.browser.find_elements_by_class_name("staff-employee")]
            name=''.join(Names)
            numbers=[int(s) for s in re.findall('\\d+',name)]
            
        except TimeoutException:
            OK=False
            
        self.browser.find_element_by_id("act_primary").click()
        try:
            FirstName = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, '_asf1')))
        except TimeoutException:
            OK=False
        NewNumber=1+max(numbers)
        for i in range(1,7):
            self.browser.find_element_by_id("_asf"+str(i)).send_keys('Cira'+str(i+NewNumber))
            self.browser.find_element_by_id("_asl"+str(i)).send_keys('Tapalaga'+str(i+NewNumber))
            self.browser.find_element_by_id("_ase"+str(i)).send_keys('cira'+str(i+NewNumber)+'@gmail.com')

        self.browser.find_element_by_id("_as_save_multiple").click()
        try:
            FirstName = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID, '_status')))
        except TimeoutException:
            OK=False

        self.assertTrue(OK)

    def tearDown(self):
        self.browser.quit()

class ChromeTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://itsolutions8.humanity.com/app/')
        self.browser.find_element_by_id("email").send_keys('irinelko@gmail.com')
        self.browser.find_element_by_id("password").send_keys('Humanity')
        self.browser.find_element_by_id("password").submit()
        try:
            logedIn = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'primNavQtip__inner')))
        except TimeoutException:
            print("Browser not responding.")
        
    def test_clock_in_chrome(self):
        FirefoxTest.test_Clock_IN_OUT(self)

    def test_add_in_chrome(self):
        FirefoxTest.test_Add_Employee(self)

    def tearDown(self):
        self.browser.quit()
    
if __name__ == "__main__":
    unittest.main()
