from selenium.webdriver.common.by import By

from base.driver_extension import DriverExtension


class HomePage(DriverExtension):
    _google_logo = (By.ID, 'hplogo')

    def is_google_displayed(self):
        return self.is_element_visible(self._google_logo)