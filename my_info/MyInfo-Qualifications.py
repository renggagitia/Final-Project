from ctypes import Union
import re
import time
import unittest
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = "Admin"
password = "admin123"

class TestMyInfoe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="D:\Program Files\geckodriver.exe")

    # Menambah Work Experience
    def test_work_experience(self):
        browser = self.driver
       
        # Login
        browser.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(1)
        browser.find_element(By.ID,"txtUsername").send_keys(user)
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        # Masuk menu My Info > Qualifications
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewMyDetails")
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/ul/li[10]").click()
        time.sleep(2)
        browser.find_element(By.ID, "addWorkExperience").click()
        time.sleep(2)
        
        # Isi required form
        browser.find_element(By.ID, "experience_employer").send_keys("My Company")
        browser.find_element(By.ID, "experience_jobtitle").send_keys("Supervisor")
        time.sleep(1)
        browser.find_element(By.ID, "btnWorkExpSave").click()
        time.sleep(3)

        responseData = browser.current_url
        self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/index.php/pim/viewQualifications/empNumber/"+('\d'))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()