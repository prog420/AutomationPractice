import allure
from tests.base_case import BaseCase
from src.pages import NotificationPage


@allure.feature("Notifications")
class TestAddRemoveElements(BaseCase):
    @allure.title("TC 03.001 User Is Able Open Notifications Page")
    def test_03_001_able_to_open_page(self):
        notif_page = NotificationPage(self.driver)
        notif_page.open()
        assert notif_page.is_opened()

    @allure.title(
        "TC 03.002 Success notification is displayed "
        "after click on 'Click here' button"
    )
    def test_03_002_success_notif_is_displayed_after_click_here(self):
        notif_page = NotificationPage(self.driver)
        notif_page.open()
        notif_page.show_notification()
        assert notif_page.is_success_notification_displayed()
