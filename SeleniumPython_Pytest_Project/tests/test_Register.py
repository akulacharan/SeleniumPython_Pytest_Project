from _datetime import datetime
import pytest
import time
from selenium.webdriver.common.by import By
from conftest import setup_and_teardown

@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class Test_register:
    def test_create_account_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("konidela")
        self.driver.find_element(By.NAME, "lastname").send_keys("Chirenjeevi")
        self.driver.find_element(By.NAME, "email").send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.NAME, "telephone").send_keys("9876543210")
        self.driver.find_element(By.NAME, "password").send_keys("123456789")
        self.driver.find_element(By.NAME, "confirm").send_keys("123456789")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH, "//div/h1[text()='Your Account Has Been Created!']").is_displayed()



    def test_create_account_with_all_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("konidela")
        self.driver.find_element(By.NAME, "lastname").send_keys("Chirenjeevi")
        self.driver.find_element(By.NAME, "email").send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.NAME, "telephone").send_keys("9876543210")
        self.driver.find_element(By.NAME, "password").send_keys("123456789")
        self.driver.find_element(By.NAME, "confirm").send_keys("123456789")
        self.driver.find_element(By.NAME, "newsletter").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH, "//div/h1[text()='Your Account Has Been Created!']").is_displayed()




    def generate_email_time_stamp(self):
        # Generate timestamp with underscores instead of hyphens
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "charan"+timestamp+"@gmail.com"
