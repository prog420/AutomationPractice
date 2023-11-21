import allure
from src.locators import NotificationLocators
from src.base import BasePage
from src.links import Links


class NotificationPage(BasePage):
    PAGE_URL = Links.NOTIFICATION_PAGE
    LOCATORS = NotificationLocators()

    @property
    def btn_show_notification(self):
        return self.find_element(self.LOCATORS.BTN_SHOW_NOTIFICATION)

    @property
    def notification_success(self):
        return self.find_element(self.LOCATORS.NOTIFICATION_SUCCESS)

    @allure.step("Show notification message")
    def show_notification(self):
        self.btn_show_notification.click()

    @allure.step("Check if success notification message is displayed")
    def is_success_notification_displayed(self):
        return self.is_element_present(self.LOCATORS.NOTIFICATION_SUCCESS)
