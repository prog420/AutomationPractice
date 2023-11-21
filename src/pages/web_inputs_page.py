import allure
from src.locators import WebInputsPageLocators
from src.base import BasePage
from src.links import Links


class WebInputsPage(BasePage):
    PAGE_URL = Links.WEB_INPUT_PAGE
    LOCATORS = WebInputsPageLocators()

    @property
    def input_number(self):
        return self.find_element(self.LOCATORS.INPUT_NUMBER)

    @property
    def input_text(self):
        return self.find_element(self.LOCATORS.INPUT_TEXT)

    @property
    def input_password(self):
        return self.find_element(self.LOCATORS.INPUT_PWD)

    @property
    def input_date(self):
        return self.find_element(self.LOCATORS.INPUT_DATE)

    @property
    def output_number(self):
        return self.find_element(self.LOCATORS.OUTPUT_NUMBER)

    @property
    def output_text(self):
        return self.find_element(self.LOCATORS.OUTPUT_TEXT)

    @property
    def output_password(self):
        return self.find_element(self.LOCATORS.OUTPUT_PWD)

    @property
    def output_date(self):
        return self.find_element(self.LOCATORS.OUTPUT_DATE)

    @property
    def btn_display_inputs(self):
        return self.find_element(self.LOCATORS.BTN_DISPLAY_INPUTS)

    @property
    def btn_clear_inputs(self):
        return self.find_element(self.LOCATORS.BTN_CLEAR_INPUTS)

    @allure.step("Display form inputs")
    def display_inputs(self):
        self.btn_display_inputs.click()

    @allure.step("Fill input field for numbers")
    def fill_number_field(self, value: str):
        self.input_number.clear()
        self.input_number.send_keys(value)

    @allure.step("Fill input field for text")
    def fill_text_field(self, value: str):
        self.input_text.clear()
        self.input_text.send_keys(value)

    @allure.step("Fill input field for passwords")
    def fill_password_field(self, value: str):
        self.input_password.clear()
        self.input_password.send_keys(value)

    @allure.step("Fill input field for date")
    def fill_date_field(self, value: str):
        self.input_date.clear()
        self.input_date.send_keys(value)
