import allure
import data
import pytest
from pages.order_page import OrderPage


class TestOrder:
    @allure.title('Проверка успешного создания заказа')
    @allure.description("Переходим на страницу созданя заказа, заполняем все необходимы поля и создаем заказ")
    def test_success_order(self, driver):
        order_page = OrderPage(driver=driver, url=data.BASE_URL)
        order_page.open_scooter_main_page()
        order_page.wait_open_page()
        order_page.click_order_button_on_main_page()
        order_page.wait_open_order_page()
        order_page.fill_first_step_form_order()
        order_page.click_go_next()
        order_page.wait_next_step_order_page()
        order_page.fill_second_step_form_order()
        order_page.click_order_button_on_order_form_page()
        order_page.wait_confirm_window_order()
        order_page.click_yes_button()
        order_page.wait_success_window_order()
        order_page.click_сheck_status()
