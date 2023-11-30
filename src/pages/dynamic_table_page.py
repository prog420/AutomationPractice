import allure
from src.locators import DynamicTableLocators
from src.base import BasePage
from src.links import Links


class DynamicTablePage(BasePage):
    PAGE_URL = Links.DYNAMIC_TABLE_PAGE
    LOCATORS = DynamicTableLocators()

    @property
    def chrome_cpu_value(self):
        chrome_cpu_value = self.find_element(self.LOCATORS.TEXT_CHROME_CPU)
        numeric_value = chrome_cpu_value.text.split()[-1]
        return numeric_value

    @allure.step("Get cell value for header '{header} and row '{row}'")
    def get_cell_value_by_header_and_row(self, header="", row=""):
        row_locator = self.LOCATORS.format_locator(
            self.LOCATORS.TABLE_ROW, row
        )
        headers = [
            element.text
            for element in self.find_elements(self.LOCATORS.TABLE_HEADERS)
        ]
        row = [element.text for element in self.find_elements(row_locator)]
        return row[headers.index(header)]
