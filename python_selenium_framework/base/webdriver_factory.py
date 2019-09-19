from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeDriverManager
from selenium import webdriver

from config import BASE_URL


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        if self.browser.lower() == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif self.browser.lower() == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.browser.lower() == "edge":
            driver = webdriver.Edge(EdgeDriverManager().install())
        elif self.browser.lower() == "ie":
            driver = webdriver.Ie(IEDriverManager().install())
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(BASE_URL)
        return driver
