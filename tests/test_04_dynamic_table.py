import allure
import pytest
from tests.base_case import BaseCase
from src.pages import DynamicTablePage


@pytest.mark.wip
@allure.feature("Dynamic Table")
class TestDynamicTable(BaseCase):
    @allure.title("TC 04.001 User Is Able Open Dynamic Table Page")
    def test_04_001_able_to_open_page(self):
        table_page = DynamicTablePage(self.driver)
        table_page.open()
        assert table_page.is_opened()

    @allure.title(
        "TC 04.002 'Chrome' - 'CPU' cell value is equal to output string"
    )
    def test_04_002_chrome_cpu_table_value_is_equal_to_output_value(self):
        table_page = DynamicTablePage(self.driver)
        table_page.open()
        chrome_cpu_table_value = table_page.get_cell_value_by_header_and_row(
            header="CPU", row="Chrome"
        )
        assert chrome_cpu_table_value == table_page.chrome_cpu_value
