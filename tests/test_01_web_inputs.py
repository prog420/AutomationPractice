import pytest
import allure
from tests.base_case import BaseCase
from src.pages import WebInputsPage


@allure.feature("Web Inputs")
class TestWebInputs(BaseCase):
    @allure.title("TC 01.001 User Is Able To Open Web Inputs Page")
    def test_01_001_able_to_open_page(self):
        web_inp_page = WebInputsPage(self.driver)
        web_inp_page.open()
        assert web_inp_page.is_opened()

    @allure.title("TC 01.002 User Is Able To Fill Number Input (pos)")
    @pytest.mark.parametrize("value", ["-9999", "-1", "0", "1", "9999"])
    def test_01_002_able_to_fill_num_field(self, value):
        web_inp_page = WebInputsPage(self.driver)
        web_inp_page.open()
        web_inp_page.fill_number_field(value)
        web_inp_page.display_inputs()
        assert web_inp_page.output_number.text == value
        assert web_inp_page.input_number.get_attribute("value") == value

    @allure.title("TC 01.003 User Is Able To Fill Text Input (pos)")
    @pytest.mark.parametrize("value", ["text", "text 999"])
    def test_01_003_able_to_fill_text_field(self, value):
        web_inp_page = WebInputsPage(self.driver)
        web_inp_page.open()
        web_inp_page.fill_text_field(value)
        web_inp_page.display_inputs()
        assert web_inp_page.output_text.text == value
        assert web_inp_page.input_text.get_attribute("value") == value

    @allure.title("TC 01.004 User Is Able To Fill Password Input (pos)")
    @pytest.mark.parametrize("value", ["qwerty123", "qwerty_123"])
    def test_01_004_able_to_fill_text_field(self, value):
        web_inp_page = WebInputsPage(self.driver)
        web_inp_page.open()
        web_inp_page.fill_password_field(value)
        web_inp_page.display_inputs()
        assert web_inp_page.output_password.text == value
        assert web_inp_page.input_password.get_attribute("value") == value

    @allure.title("TC 01.005 User Is Able To Fill Date Input (pos)")
    @pytest.mark.parametrize(
        "date_input, expected_output", [("12-30-1995", "1995-12-30")]
    )
    def test_01_005_able_to_fill_date_field(self, date_input, expected_output):
        """
        Acceptable format for Date: "mm-dd-yyyy" / "mmddyyyy"
        """
        web_inp_page = WebInputsPage(self.driver)
        web_inp_page.open()
        web_inp_page.fill_date_field(date_input)
        web_inp_page.display_inputs()
        assert web_inp_page.output_date.text == expected_output
        assert web_inp_page.input_date.get_attribute("value") == expected_output
