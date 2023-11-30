import allure
from src.locators import BrowserInfoPageLocators
from src.base import BasePage
from src.links import Links


class BrowserInfoPage(BasePage):
    PAGE_URL = Links.BROWSER_INFO_PAGE
    LOCATORS = BrowserInfoPageLocators()

    @property
    def btn_toggle_info(self):
        return self.find_element(self.LOCATORS.BTN_TOGGLE_INFO)

    @property
    def text_user_agent(self):
        return self.find_element(self.LOCATORS.TEXT_USER_AGENT).text

    @property
    def text_browser_name(self):
        return self.find_element(self.LOCATORS.TEXT_BROWSER_NAME).text

    @property
    def text_platform(self):
        return self.find_element(self.LOCATORS.TEXT_PLATFORM).text

    @property
    def text_cookie(self):
        return self.find_element(self.LOCATORS.TEXT_BROWSER_COOKIE).text

    @allure.step("Toggle browser information")
    def toggle_browser_info(self):
        self.btn_toggle_info.click()

    @allure.step("Check if browser info is displayed")
    def is_browser_info_displayed(self):
        return self.is_element_present(self.LOCATORS.TABLE_BROWSER_INFO)
