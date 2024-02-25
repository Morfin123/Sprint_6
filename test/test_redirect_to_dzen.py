import allure
import data
from pages.order_page import OrderPage


class TestRedirectToDzen:
    @allure.title('Проверка перехода на страницу Дзена')
    @allure.description(
        'Нажимаем на "Яндекс" в шапке главной страниы и проверяем переход на соответствующий URL'
    )
    def test_redirect_to_dzen(self, driver):
        page = OrderPage(driver=driver, url=data.BASE_URL)
        page.open_scooter_main_page()
        page.wait_open_page()
        page.click_to_yandex_in_header()
        page.check_redirect_to_dzen()
