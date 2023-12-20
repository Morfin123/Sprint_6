import allure
import pytest
import data
from pages.order_page import OrderPageHelper
from pages.question_page import QuestionPageHelper


class TestQuestions:
    @allure.title('Проверка выпадающих ответов на главной странице "Яндекс Самокат"')
    @allure.description("Находим раздел с вопросами и проверяем, что выпадающий ответ соотвтетсует вопросу")
    @pytest.mark.parametrize('question, answer, text_answer', data.DataQuestionPage.question_test_params)
    def test_questions_on_main_page(self, driver, question, answer, text_answer):
        question_page = QuestionPageHelper(driver=driver, url=data.BASE_URL)
        question_page.open_scooter_main_page()
        question_page.scroll_page_to_questions(question)
        question_page.click_on_question(question)
        question_answer = question_page.get_drop_down_text_answer(answer)
        assert question_answer == text_answer, "Ответ не соответствует вопросу"


class TestOrder:
    @allure.title('Проверка успешного создания заказа')
    @allure.description("Переходим на страницу созданя заказа, заполняем все необходимы поля и создаем заказ")
    #@pytest.mark.parametrize('order_button', data.order_button)
    def test_success_order(self, driver):
        order_page = OrderPageHelper(driver=driver, url=data.BASE_URL)
        order_page.open_scooter_main_page()
        order_page.wait_open_page()
        order_page.click_order_button()
        order_page.wait_open_order_page()
        order_page.insert_input_firstname()
        order_page.insert_input_lastname()
        order_page.insert_input_address()
        order_page.insert_input_metro()
        order_page.insert_input_phone()
        order_page.click_go_next()
        order_page.wait_next_step_order_page()
        order_page.insert_input_date_delivery()
        order_page.insert_input_time_rental()
        order_page.choose_scooter_colour()
        order_page.insert_input_comment()
        order_page.click_order_button()
        order_page.wait_confirm_window_order()
        order_page.click_yes_button()
        order_page.wait_success_window_order()
        order_page.click_сheck_status()
        order_page.wait_open_created_order_page()
        order_page.click_to_yandex_in_header()
        order_page.check_redirect_to_dzen()
        order_page.click_scooter_to_dzen()
        order_page.check_main_url_scooter_page()
