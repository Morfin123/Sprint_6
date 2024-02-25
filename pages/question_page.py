import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage


class QuestionPageLocators:
    # Локаторы вопросов на главной
    HOW_MUCH = [By.XPATH, '//div[text()="Сколько это стоит? И как оплатить?"]']
    WANT_A_LOT = [By.XPATH, '//div[text()="Хочу сразу несколько самокатов! Так можно?"]']
    RENTAL_TIME = [By.XPATH, '//div[text()="Как рассчитывается время аренды?"]']
    ORDER_TODAY = [By.XPATH, '//div[text()="Можно ли заказать самокат прямо на сегодня?"]']
    EXTEND_OR_REFUND = [By.XPATH, '//div[text()="Можно ли продлить заказ или вернуть самокат раньше?"]']
    NECESSARY_CHARGE = [By.XPATH, '//div[text()="Вы привозите зарядку вместе с самокатом?"]']
    CANCEL_ORDER = [By.XPATH, '//div[text()="Можно ли отменить заказ?"]']
    DELIVERY_RANGE = [By.XPATH, '//div[text()="Я жизу за МКАДом, привезёте?"]']

    # Локаторы ответов на вопросы
    ANSWER_HOW_MUCH = [By.XPATH, "//p[contains(text(), 'Сутки — 400 рублей. Оплата курьеру')]"]
    ANSWER_WANT_A_LOT = [By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ')]"]
    ANSWER_RENTAL_TIME = [By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая')]"]
    ANSWER_ORDER_TODAY = [By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего')]"]
    ANSWER_EXTEND_OR_REFUND = [By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное')]"]
    ANSWER_NECESSARY_CHARGE = [By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной')]"]
    ANSWER_CANCEL_ORDER = [By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли. Штрафа')]"]
    ANSWER_DELIVERY_RANGE = [By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве')]"]


class QuestionPageHelper(BasePage):
    @allure.step('Открыть главную страницу "Яндекс Самокат"')
    def open_scooter_main_page(self):
        return self.open_page()

    @allure.step('Проскроллить страницу к разделу "Вопросы о важном"')
    def scroll_page_to_questions(self, question):
        question_on_page = self.find_element_with_wait(question)
        return self.scroll_to_element(question_on_page)

    @allure.step('Нажать на вопрос')
    def click_on_question(self, question):
        return self.click_on_element(question)

    @allure.step('Получить текст ответа')
    def get_drop_down_text_answer(self, answer):
        return self.get_text_from_element(answer)


