from pages.home_page import HomePage


class PageManager:
    def __init__(self, driver):
        self.driver = driver

    @property
    def home_page(self) -> HomePage:
        return HomePage(self.driver)
