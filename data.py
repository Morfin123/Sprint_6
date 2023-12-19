from pages.question_page import QuestionPageLocators


BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
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
