import allure
from src.locators import AddRemovePageLocators
from src.base import BasePage
from src.links import Links


class AddRemovePage(BasePage):
    PAGE_URL = Links.ADD_REMOVE_PAGE
    LOCATORS = AddRemovePageLocators()

    @property
    def btn_add_element(self):
        return self.find_element(self.LOCATORS.BTN_ADD_ELEMENT)

    @property
    def btn_remove_element(self):
        return self.find_element(self.LOCATORS.BTN_REMOVE_ELEMENT)

    @property
    def btns_remove_element(self):
        return self.find_elements(self.LOCATORS.BTN_REMOVE_ELEMENT)

    @allure.step("Add element")
    def add_element(self):
        self.btn_add_element.click()

    @allure.step("Remove element")
    def remove_element(self):
        self.btn_remove_element.click()

    @allure.step("Add multiple elements")
    def add_elements(self, num_of_elements: int):
        for i in range(num_of_elements):
            self.add_element()

    @allure.step("Remove all elements")
    def remove_all_elements(self):
        for button in self.btns_remove_element:
            button.click()

    @allure.step("Check if all elements removed")
    def is_elements_removed(self):
        return self.is_not_element_present(self.LOCATORS.BTN_REMOVE_ELEMENT)
