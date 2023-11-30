from selenium.webdriver.common.by import By
from src.base.base_locators import BasePageLocators


class BrowserInfoPageLocators(BasePageLocators):
    BTN_TOGGLE_INFO = (By.CSS_SELECTOR, 'button[id="browser-toggle"]')
    TEXT_USER_AGENT = (By.CSS_SELECTOR, 'td[id="browser-user-agent"]')
    TEXT_BROWSER_NAME = (By.CSS_SELECTOR, 'td[id="browser-name"]')
    TEXT_PLATFORM = (By.CSS_SELECTOR, 'td[id="browser-platform"]')
    TEXT_BROWSER_COOKIE = (By.CSS_SELECTOR, 'td[id="browser-cookie"]')
    TABLE_BROWSER_INFO = (By.XPATH, '//div[@id="browser-info"]//table')
