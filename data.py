from pages.order_page import OrderPageLocators
from pages.question_page import QuestionPageLocators
BASE_URL = 'https://qa-scooter.praktikum-services.ru/'


class DataQuestionPage:
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

    # Набор вопросов и ответов
    question_test_params = [
        [
            QuestionPageLocators.HOW_MUCH,
            QuestionPageLocators.ANSWER_HOW_MUCH,
            text_answer_how_much
        ],
        [
            QuestionPageLocators.WANT_A_LOT,
            QuestionPageLocators.ANSWER_WANT_A_LOT,
            text_answer_want_a_lot
        ],
        [
            QuestionPageLocators.RENTAL_TIME,
            QuestionPageLocators.ANSWER_RENTAL_TIME,
            text_answer_rental_time
        ],
        [
            QuestionPageLocators.ORDER_TODAY,
            QuestionPageLocators.ANSWER_ORDER_TODAY,
            text_answer_order_today
        ],
        [
            QuestionPageLocators.EXTEND_OR_REFUND,
            QuestionPageLocators.ANSWER_EXTEND_OR_REFUND,
            text_answer_extend_or_refund
        ],
        [
            QuestionPageLocators.NECESSARY_CHARGE,
            QuestionPageLocators.ANSWER_NECESSARY_CHARGE,
            text_answer_necessary_charge
        ],
        [
            QuestionPageLocators.CANCEL_ORDER,
            QuestionPageLocators.ANSWER_CANCEL_ORDER,
            text_answer_cancel_order
        ],
        [
            QuestionPageLocators.DELIVERY_RANGE,
            QuestionPageLocators.ANSWER_DELIVERY_RANGE,
            text_answer_delivery_range
        ]
    ]
