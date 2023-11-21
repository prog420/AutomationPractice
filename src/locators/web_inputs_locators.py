from selenium.webdriver.common.by import By
from src.base.base_locators import BasePageLocators


class WebInputsPageLocators(BasePageLocators):
    BTN_DISPLAY_INPUTS = (By.CSS_SELECTOR, "button#btn-display-inputs")
    BTN_CLEAR_INPUTS = (By.CSS_SELECTOR, "button#btn-clear-inputs")
    INPUT_NUMBER = (By.CSS_SELECTOR, "input#input-number")
    INPUT_TEXT = (By.CSS_SELECTOR, "input#input-text")
    INPUT_PWD = (By.CSS_SELECTOR, "input#input-password")
    INPUT_DATE = (By.CSS_SELECTOR, "input#input-date")
    OUTPUT_NUMBER = (By.CSS_SELECTOR, "strong#output-number")
    OUTPUT_TEXT = (By.CSS_SELECTOR, "strong#output-text")
    OUTPUT_PWD = (By.CSS_SELECTOR, "strong#output-password")
    OUTPUT_DATE = (By.CSS_SELECTOR, "strong#output-date")
