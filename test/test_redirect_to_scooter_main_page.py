import allure
import data
from pages.order_page import OrderPage


class TestRedirectToScooterMainPage:
    @allure.title('Проверка перехода на лавную странимце ЯндексСамокат')
    @allure.description(
        'Нажимаем на "Самокат" в шапке главной страниы и проверяем переход на соответствующий URL'
    )
    def test_redirect_to_dzen(self, driver):
        page = OrderPage(driver=driver, url=data.BASE_URL)
        page.open_scooter_main_page()
        page.wait_open_page()
        page.click_order_button_on_main_page()
        page.click_scooter_on_header()
        page.check_main_url_scooter_page()
