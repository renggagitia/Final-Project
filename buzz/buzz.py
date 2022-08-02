from ctypes import Union
import time
import unittest
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = "Admin"
password = "admin123"

class TestBuzz(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="D:\Program Files\geckodriver.exe")

    # Filter daftar Directory dengan kriteria Job Title
    def test_post_status(self):
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

        # Masuk menu Buzz
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/buzz/viewBuzz")
        time.sleep(2)
        
        # Isi status
        browser.find_element(By.ID,"createPost_content").send_keys("Test status update")
        time.sleep(1)
        browser.find_element(By.ID,"postSubmitBtn").click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()