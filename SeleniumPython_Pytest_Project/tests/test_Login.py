from selenium.webdriver.common.by import By
from conftest import setup_and_teardown
import pytest
import time

@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class Test_login:

    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH,"//a[text()='Login']").click()
        self.driver.find_element(By.NAME,"email").send_keys("akulacharanteja@gmail.com")
        self.driver.find_element(By.NAME,"password").send_keys("123456789")
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        time.sleep(2)

        assert self.driver.find_element(By.XPATH,"//a[text()='Edit your account information']").is_displayed()


    def test_login_without_entering_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
        self.driver.find_element(By.NAME, "email").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)

        assert self.driver.find_element(By.XPATH, "//div[text()='Warning: No match for E-Mail Address and/or Password.']").is_displayed()

