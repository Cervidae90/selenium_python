import pytest

from base.base_test import BaseTest


class TestMain(BaseTest):
    @pytest.fixture(autouse=True)
    def init(self, driver):
        super().init(driver)

    def test_google_is_displayed_on_home_page(self):
        assert True is self.pages.home_page.is_google_displayed()
