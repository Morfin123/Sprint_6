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

    # Текст ответов
    text_answer_how_much = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    text_answer_want_a_lot = ("Пока что у нас так: один заказ — один самокат. "
                              "Если хотите покататься с друзьями, можете просто сделать несколько заказов — "
                              "один за другим.")

    text_answer_rental_time = ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
                               "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
                               "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")

    text_answer_order_today = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    text_answer_extend_or_refund = ("Пока что нет! Но если что-то срочное — "
                                    "всегда можно позвонить в поддержку по красивому номеру 1010.")

    text_answer_necessary_charge = ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — "
                                    "даже если будете кататься без передышек и во сне. Зарядка не понадобится.")

    text_answer_cancel_order = ("Да, пока самокат не привезли. Штрафа не будет, "
                                "объяснительной записки тоже не попросим. Все же свои.")

    text_answer_delivery_range = "Да, обязательно. Всем самокатов! И Москве, и Московской области."


class QuestionPageHelper(BasePage):
    @allure.step('Открыть главную страницу "Яндекс Самокат"')
    def open_scooter_main_page(self):
        return self.driver.get(self.url)

    @allure.step('Проскроллить страницу к разделу "Вопросы о важном"')
    def scroll_page_to_questions(self, question):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (question)))
        question_on_page = self.driver.find_element(*question)
        return self.driver.execute_script("arguments[0].scrollIntoView();", question_on_page)

    @allure.step('Нажать на вопрос')
    def click_on_question(self, question):
        return WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
            (question))).click()

    @allure.step('Получить текст ответа')
    def get_drop_down_text_answer(self, answer):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (answer))).text


