import allure
import pytest
from tests.base_case import BaseCase
from src.pages import BrowserInfoPage


@allure.feature("Browser Information")
class TestDynamicTable(BaseCase):
    @allure.title("TC 05.001 User Is Able Open Browser Information Page")
    def test_05_001_able_to_open_page(self):
        info_page = BrowserInfoPage(self.driver)
        info_page.open()
        assert info_page.is_opened()

    @allure.title(
        "TC 05.002 User is able to see browser information"
    )
    def test_05_002_chrome_cpu_table_value_is_equal_to_output_value(self):
        info_page = BrowserInfoPage(self.driver)
        info_page.open()
        info_page.toggle_browser_info()
        assert info_page.is_browser_info_displayed()

    @allure.title(
        "TC 05.003 'User Agent' is equal to browser's user-agent"
    )
    def test_05_003_displayed_user_agent_is_equal_to_browser_u_a(self):
        info_page = BrowserInfoPage(self.driver)
        info_page.open()
        info_page.toggle_browser_info()
        with allure.step("Check if displayed user agent is "
                         "equal to browser's user agent"):
            assert info_page.get_user_agent() == info_page.text_user_agent

    @allure.title(
        "TC 05.004 'Cookies enabled' value is equal to browser settings value"
    )
    def test_05_004_cookie_enabled_is_equal_to_browser_settings(self):
        info_page = BrowserInfoPage(self.driver)
        info_page.open()
        info_page.toggle_browser_info()
        with allure.step(
                "Check if 'Cookie Enabled' value is equal to value from "
                "browser settings"):
            assert str(self.config.cookie_enabled).lower() == \
                   info_page.text_cookie
