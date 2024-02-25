import allure
import pytest
import data
from pages.question_page import QuestionPage


class TestQuestions:
    @allure.title('Проверка выпадающих ответов на главной странице "Яндекс Самокат"')
    @allure.description("Находим раздел с вопросами и проверяем, что выпадающий ответ соотвтетсует вопросу")
    @pytest.mark.parametrize('question, answer, text_answer', data.DataQuestionPage.question_test_params)
    def test_questions_on_main_page(self, driver, question, answer, text_answer):
        question_page = QuestionPage(driver=driver, url=data.BASE_URL)
        question_page.open_scooter_main_page()
        question_page.scroll_page_to_questions(question)
        question_page.click_on_question(question)
        question_answer = question_page.get_drop_down_text_answer(answer)
        assert question_answer == text_answer, "Ответ не соответствует вопросу"
