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

    # Cari Username semua User Role
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
        # Masuk menu Admin > User Management > Users
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")
        time.sleep(2)
        
        browser.find_element(By.ID, "searchSystemUser_userName").send_keys("aravind")
        time.sleep(1)
        browser.find_element(By.ID, "searchBtn").click()
        time.sleep(2)

        responseData = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]/a").text
        # print(responseData)
        self.assertIn(responseData, "Aravind")
        
    # Cari Username kriteria User Role Admin
    # Cari Username kriteria User Role ESS
    # Cari Username kriteria Status Enabled
    # Cari Username kriteria Status Disabled
    # Filter daftar User dengan kriteria User Role Admin
    # Filter daftar User dengan kriteria User Role ESS
    # Filter daftar User dengan kriteria Status Enabled
    # Filter daftar User dengan kriteria Status Disabled

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()