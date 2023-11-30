from selenium.webdriver.common.by import By
from src.base.base_locators import BasePageLocators


class DynamicTableLocators(BasePageLocators):
    TABLE_HEADERS = (By.CSS_SELECTOR, "thead>tr>th")
    TABLE_ROW = (By.XPATH, '//td[parent::tr/td/text()="{}"]')
    TEXT_CHROME_CPU = (By.CSS_SELECTOR, 'p[id="chrome-cpu"]')
