from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import NORMAL


class DriverExtension:
    wait_time = NORMAL

    def __init__(self, driver):
        self.driver = driver

    def send_keys(self, element, value, time=wait_time):
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(element)
        )
        self.driver.find_element(*element).send_keys(value)

    def click_element(self, element, time=wait_time):
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(element)
        )
        WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(element)
        )
        self.driver.find_element(*element).click()

    def is_element_visible(self, element, time=wait_time):
        try:
            WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(element)
            )
            return True
        except TimeoutException:
            return False
