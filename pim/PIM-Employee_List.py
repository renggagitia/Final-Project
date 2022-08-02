from ctypes import Union
import time
import unittest
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = "Admin"
password = "admin123"

class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="D:\Program Files\geckodriver.exe")

    # Tambah Employee
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
        # Masuk menu PIM > Employee List
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployeeList/")
        time.sleep(2)
        
        browser.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
        browser.find_element(By.ID,"firstName").send_keys("Lewin")
        time.sleep(1)
        browser.find_element(By.ID,"lastName").send_keys("Joyce")
        time.sleep(1)
        browser.find_element(By.ID, "btnSave").click()
        time.sleep(2)

        responseData = browser.current_url
        self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/index.php/pim/viewPersonalDetails/empNumber/"+('\d'))

    # Tambah Employee dengan Employee Id yang sudah ada
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
        # Masuk menu PIM > Employee List
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployeeList/")
        time.sleep(3)
        # Capture salah satu Id
        capturedId = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr[1]/td[2]/a").text
        
        browser.find_element(By.ID, "btnAdd").click()
        time.sleep(2)
        browser.find_element(By.ID,"firstName").send_keys("Lewin")
        time.sleep(1)
        browser.find_element(By.ID,"lastName").send_keys("Joyce")
        time.sleep(1)
        browser.find_element(By.ID,"employeeId").clear()
        time.sleep(1)
        browser.find_element(By.ID,"employeeId").send_keys(capturedId)
        time.sleep(1)
        browser.find_element(By.ID, "btnSave").click()
        time.sleep(2)

        responseData = browser.current_url
        self.assertIn(responseData, "https://opensource-demo.orangehrmlive.com/index.php/pim/addEmployee")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()