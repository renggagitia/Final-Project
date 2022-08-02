from ctypes import Union
import time
import unittest
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = "Admin"
password = "admin123"

class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="D:\Program Files\geckodriver.exe")

    # Filter daftar Directory dengan kriteria Job Title
    def test_filter_job_title(self):
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

        # Masuk menu Directory
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/directory/viewDirectory")
        time.sleep(2)
        
        # Isi form
        kriteria = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/select/option[11]").text
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/select/option[11]").click() # Database Administrator
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)
        
        responseData = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/table/tbody/tr[2]/td[2]/ul/li[2]").text
        self.assertIn(responseData, kriteria)

    # Filter daftar Directory dengan kriteria Location
    def test_filter_locaion(self):
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

        # Masuk menu Directory
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/directory/viewDirectory")
        time.sleep(2)
        
        # Isi form
        kriteria = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[3]/select/option[3]").text
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[3]/select/option[3]").click()
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)
        
        responseData = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/table/tbody/tr[2]/td[2]/ul/li[4] ").text
        self.assertIn(responseData, kriteria)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()