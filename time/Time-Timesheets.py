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

class TestTime(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="D:\Program Files\geckodriver.exe")

    # Approve Timesheet Employee
    def test_cari_username(self):
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

        # Masuk menu Time > Timesheets > Empolyee Timesheets
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/time/viewEmployeeTimesheet")
        time.sleep(2)
        
        # Pilih view employee
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/table/tbody/tr[1]/td[3]").click()
        time.sleep(2)
        browser.find_element(By.ID,"btnApprove").click()
        time.sleep(2)

        responseData = browser.find_element(By.ID, "timesheet_status").text
        self.assertIn(responseData, "Status: Approved")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()