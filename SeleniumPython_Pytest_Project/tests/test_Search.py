import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from conftest import setup_and_teardown
@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class Test_search():

    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_for_a_valid_Product(self):
        self.driver.find_element(By.NAME, "search").send_keys("Hp")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        time.sleep(4)
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(),name="Valid Search",attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.MINOR)
    def test_search_for_an_Invalid_Product(self):
        self.driver.find_element(By.NAME, "search").send_keys("Hpjkl")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        time.sleep(2)
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
        allure.attach(self.driver.get_screenshot_as_png(), name="InValid Search",attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_search_without_providing_any_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        time.sleep(2)
        expected_text = "There is no product that matches the search criteria."

        assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
        allure.attach(self.driver.get_screenshot_as_png(), name="Empty Search",attachment_type=AttachmentType.PNG)