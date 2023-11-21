import allure
from tests.base_case import BaseCase
from src.pages import AddRemovePage


@allure.feature("Adding / Removing Elements")
class TestAddRemoveElements(BaseCase):
    @allure.title("TC 02.001 User Is Able Open Add/Remove Elements Page")
    def test_02_001_able_to_open_page(self):
        add_rm_page = AddRemovePage(self.driver)
        add_rm_page.open()
        assert add_rm_page.is_opened()

    @allure.title("TC 02.002 User Is Able To Add And Remove Elements")
    def test_02_002_able_to_add_remove_elements(self):
        add_rm_page = AddRemovePage(self.driver)
        add_rm_page.open()
        add_rm_page.add_elements(num_of_elements=5)
        add_rm_page.remove_all_elements()
        assert add_rm_page.is_elements_removed()
