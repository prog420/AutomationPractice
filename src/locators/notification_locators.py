from selenium.webdriver.common.by import By
from src.base.base_locators import BasePageLocators


class NotificationLocators(BasePageLocators):
    BTN_SHOW_NOTIFICATION = (By.CSS_SELECTOR, 'a[href="/notification-message"]')
    NOTIFICATION_SUCCESS = (By.XPATH, '//b[text()="Action successful"]')
    NOTIFICATION_TRY_AGAIN = (
        By.XPATH,
        '//b[text()="Action unsuccessful, please try again"]',
    )
