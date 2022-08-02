from ctypes import Union
import time
import unittest
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = "Admin"
password = "admin123"

class TestLeave(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="D:\Program Files\geckodriver.exe")

    # Tambah Leave Entitlement
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

        # Masuk menu Leave > Entitlements > Add Entitlements
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/leave/addLeaveEntitlement")
        time.sleep(2)
        
        # Isi form
        browser.find_element(By.ID, "entitlements_employee_empName").send_keys("Cass")
        time.sleep(1)
        browser.find_element(By.ID, "entitlements_employee_empName").send_keys(Keys.TAB)
        time.sleep(1)
        browser.find_element(By.ID, "entitlements_entitlement").send_keys("3")
        time.sleep(1)
        browser.find_element(By.ID, "btnSave").click()
        time.sleep(5)      

        responseData = browser.current_url
        self.assertIn(responseData, "https://opensource-demo.orangehrmlive.com/index.php/leave/viewLeaveEntitlements/savedsearch/1")

    # Hapus Entitlement
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

        # Masuk menu Leave > Entitlements > Employee Entitlements
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/leave/viewLeaveEntitlements/reset/1")
        time.sleep(2)

        # Isi form
        browser.find_element(By.ID, "entitlements_employee_empName").send_keys("Cass")
        time.sleep(1)
        browser.find_element(By.ID, "entitlements_employee_empName").send_keys(Keys.TAB)
        time.sleep(1)
        browser.find_element(By.ID,"period").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[3]/select/option[1]").click()
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr[1]/td[1]").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnDelete").click()
        time.sleep(2)
        browser.find_element(By.ID,"dialogDeleteBtn").click()
        time.sleep(2)

        responseData = browser.current_url
        self.assertIn(responseData, "https://opensource-demo.orangehrmlive.com/index.php/leave/viewLeaveEntitlements/savedsearch/1")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()