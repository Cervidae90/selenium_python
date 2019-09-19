from managers.page_manager import PageManager


class BaseTest:
    pages: PageManager = None

    def init(self, driver):
        self.pages = PageManager(driver)
