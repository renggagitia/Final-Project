from ctypes import Union
import time
import unittest
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = "Admin"
password = "admin123"

class TestPerformace(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="D:\Program Files\geckodriver.exe")

    # Tambah Performance Review
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

        # Masuk menu Performance > Manage Reviews
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/performance/searchPerformancReview")
        time.sleep(2)
        browser.find_element(By.ID, "btnAdd").click()
        time.sleep(2)

        # Isi form
        browser.find_element(By.ID, "saveReview360Form_employee").send_keys("A")
        time.sleep(1)
        browser.find_element(By.ID, "saveReview360Form_employee").send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        browser.find_element(By.ID, "saveReview360Form_employee").send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        browser.find_element(By.ID, "saveReview360Form_employee").send_keys(Keys.TAB)
        time.sleep(2)
        browser.find_element(By.ID, "saveReview360Form_supervisorReviewer").send_keys("A")
        time.sleep(1)
        browser.find_element(By.ID, "saveReview360Form_supervisorReviewer").send_keys(Keys.TAB)
        time.sleep(1)
        browser.find_element(By.ID, "saveReview360Form_workPeriodStartDate").clear()
        browser.find_element(By.ID, "saveReview360Form_workPeriodEndDate").clear()
        browser.find_element(By.ID, "saveReview360Form_dueDate").clear()
        time.sleep(1)
        browser.find_element(By.ID, "saveReview360Form_workPeriodStartDate").send_keys("2017-06-01")
        browser.find_element(By.ID, "saveReview360Form_workPeriodEndDate").send_keys("2021-08-01")
        browser.find_element(By.ID, "saveReview360Form_dueDate").send_keys("2022-08-31")
        time.sleep(1)
        browser.find_element(By.ID, "saveBtn").click()
        time.sleep(2)
        
        responseData = browser.current_url
        self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/index.php/performance/searchPerformancReview")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()