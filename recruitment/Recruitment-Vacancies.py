import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

user = "Admin"
password = "admin123"

class TestRecruitment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="D:\Program Files\geckodriver.exe")

    # Membuat Vacancy baru
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

        # Masuk menu Recruitment > Vacancies
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/recruitment/viewJobVacancy")
        time.sleep(2)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        browser.find_element(By.ID,"addJobVacancy_jobTitle").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/select/option[10]").click()
        time.sleep(1)
        browser.find_element(By.ID,"addJobVacancy_name").send_keys("Application Engineer")
        time.sleep(1)
        browser.find_element(By.ID,"addJobVacancy_hiringManager").send_keys("A")
        time.sleep(1)
        browser.find_element(By.ID,"addJobVacancy_hiringManager").send_keys(Keys.TAB)
        time.sleep(1)
        browser.find_element(By.ID,"addJobVacancy_publishedInFeed").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(3)

        responseData = browser.current_url
        self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/index.php/recruitment/addJobVacancy/Id/" + ('\d'))

    # Hapus Vacancy
    # def test_cari_username(self):
    #     browser = self.driver
       
    #     # Login
    #     browser.get("https://opensource-demo.orangehrmlive.com/")
    #     time.sleep(1)
    #     browser.find_element(By.ID,"txtUsername").send_keys(user)
    #     time.sleep(1)
    #     browser.find_element(By.ID,"txtPassword").send_keys(password)
    #     time.sleep(1)
    #     browser.find_element(By.ID,"btnLogin").click()
    #     time.sleep(2)

    #     # Masuk menu Recruitment > Vacancies
    #     browser.get("https://opensource-demo.orangehrmlive.com/index.php/recruitment/viewJobVacancy")
    #     time.sleep(2)
        
    #     browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr[1]/td[1]").click()
    #     time.sleep(1)
    #     browser.find_element(By.ID,"btnDelete").click()
    #     time.sleep(1)
    #     browser.find_element(By.ID,"dialogDeleteBtn").click()
    #     time.sleep(3)

        # responseData = browser.current_url
        # self.assertRegex(responseData, "https://opensource-demo.orangehrmlive.com/index.php/recruitment/addJobVacancy/Id/" + ('\d'))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()