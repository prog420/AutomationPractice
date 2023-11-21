from selenium.webdriver.common.by import By
from src.base.base_locators import BasePageLocators


class AddRemovePageLocators(BasePageLocators):
    BTN_ADD_ELEMENT = (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    BTN_REMOVE_ELEMENT = (
        By.CSS_SELECTOR,
        'button.added-manually[onclick="deleteElement()"]',
    )
