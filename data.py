from pages.question_page import QuestionPageLocators
from datetime import date
import random
BASE_URL = 'https://qa-scooter.praktikum-services.ru/'


class DataQuestionPage:
    question_test_params = [
        [
            QuestionPageLocators.HOW_MUCH,
            QuestionPageLocators.ANSWER_HOW_MUCH,
            QuestionPageLocators.text_answer_how_much
        ],
        [
            QuestionPageLocators.WANT_A_LOT,
            QuestionPageLocators.ANSWER_WANT_A_LOT,
            QuestionPageLocators.text_answer_want_a_lot
        ],
        [
            QuestionPageLocators.RENTAL_TIME,
            QuestionPageLocators.ANSWER_RENTAL_TIME,
            QuestionPageLocators.text_answer_rental_time
        ],
        [
            QuestionPageLocators.ORDER_TODAY,
            QuestionPageLocators.ANSWER_ORDER_TODAY,
            QuestionPageLocators.text_answer_order_today
        ],
        [
            QuestionPageLocators.EXTEND_OR_REFUND,
            QuestionPageLocators.ANSWER_EXTEND_OR_REFUND,
            QuestionPageLocators.text_answer_extend_or_refund
        ],
        [
            QuestionPageLocators.NECESSARY_CHARGE,
            QuestionPageLocators.ANSWER_NECESSARY_CHARGE,
            QuestionPageLocators.text_answer_necessary_charge
        ],
        [
            QuestionPageLocators.CANCEL_ORDER,
            QuestionPageLocators.ANSWER_CANCEL_ORDER,
            QuestionPageLocators.text_answer_cancel_order
        ],
        [
            QuestionPageLocators.DELIVERY_RANGE,
            QuestionPageLocators.ANSWER_DELIVERY_RANGE,
            QuestionPageLocators.text_answer_delivery_range
        ]
    ]


class DataOrderPage:
    def get_random_time_rental():
        choice = ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток']
        random_index = random.randrange(len(choice))
        time_rental = choice[random_index]
        return time_rental

    def get_random_colour():
        choice = ['black', 'grey']
        random_index = random.randrange(len(choice))
        colour = choice[random_index]
        return colour

    def get_random_phone():
        phone = f'79{random.randint(100000000, 999999999)}'
        return phone

    def get_random_metro():
        return random.randint(1, 237)