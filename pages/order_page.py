import allure
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data_helper
from data_helper import OrderPageDataHelper
from pages.base_page import BasePage


class OrderPageLocators:

    MAIN_PAGE_LOGO = [By.CLASS_NAME, 'Header_Logo__23yGT']
    HEADER_BUTTON_ORDER = [By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]']
    PAGE_BUTTON_ORDER = [By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']
    INPUT_FIRST_NAME = [By.XPATH, '//input[@placeholder="* Имя"]']
    INPUT_LAST_NAME = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    INPUT_DELIVERY_ADDRESS = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    INPUT_METRO = [By.XPATH, '//input[@placeholder="* Станция метро"]']
    INPUT_PHONE = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    METRO = [By.XPATH, f'//li[@data-value="{OrderPageDataHelper.get_random_metro()}"]']
    GO_NEXT = [By.XPATH, '//button[text()="Далее"]']
    INPUT_DATE_DELIVERY = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    DATE_DELIVERY = [By.XPATH, f'//div[@class="react-datepicker__month"]//div[text()="{date.today().day}"]']
    SELECT_TIME_RENTAL = [By.XPATH, '//div[text()="* Срок аренды"]']
    TIME_RENTAL = [By.XPATH, f'//div[text()="{OrderPageDataHelper.get_random_time_rental()}"]']
    INPUT_COLOUR = [By.ID, f'{OrderPageDataHelper.get_random_colour()}']
    INPUT_COMMENT = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']
    BUTTON_ORDER = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']
    CONFIRM_WINDOW_ORDER = [By.CLASS_NAME, 'Order_Modal__YZ-d3']
    BUTTON_YES = [By.XPATH, '//button[text()="Да"]']
    SUCCESS_WINDOW_ORDER = [By.XPATH, '//div[text()="Заказ оформлен"]']
    BUTTON_CHECK_STATUS = [By.XPATH, '//button[text()="Посмотреть статус"]']
    BUTTON_CANCEL_ORDER = [By.XPATH, '//button[text()="Отменить заказ"]']
    HEADER_BUTTON_YANDEX = [By.XPATH, '//img[@alt="Yandex"]']
    HEADER_BUTTON_SCOOTER = [By.XPATH, '//img[@alt="Scooter"]']


class OrderPage(BasePage):

    @allure.step('Открыть главную страницу "Яндекс Самокат"')
    def open_scooter_main_page(self):
        return self.open_page()

    @allure.step('Ждем загрузку главной страницы')
    def wait_open_page(self):
        return self.find_element_with_wait(OrderPageLocators.MAIN_PAGE_LOGO)

    @allure.step('Нажимаем на кнопку "Заказать" на главной')
    def click_order_button_on_main_page(self):
        return self.click_on_element(OrderPageLocators.HEADER_BUTTON_ORDER)

    @allure.step('Ждем загрузку страницы оформления заказа')
    def wait_open_order_page(self):
        return self.find_element_with_wait(OrderPageLocators.INPUT_FIRST_NAME)

    @allure.step('Заполняем поле "Имя"')
    def insert_input_firstname(self):
        return self.send_element(OrderPageLocators.INPUT_FIRST_NAME, 'Имя')

    @allure.step('Заполняем поле "Фамилия"')
    def insert_input_lastname(self):
        return self.send_element(OrderPageLocators.INPUT_LAST_NAME, 'Фамилия')

    @allure.step('Заполняем поле "Адрес"')
    def insert_input_address(self):
        return self.send_element(OrderPageLocators.INPUT_DELIVERY_ADDRESS,'Пушкина')

    @allure.step('Заполняем поле "Станция метро"')
    def insert_input_metro(self):
        self.click_on_element(OrderPageLocators.INPUT_METRO)
        return self.click_on_element(OrderPageLocators.METRO)

    @allure.step('Заполняем поле "Телефон"')
    def insert_input_phone(self):
        return self.send_element(OrderPageLocators.INPUT_PHONE, f'{data_helper.OrderPageDataHelper.get_random_phone()}')

    @allure.story('Запоняем форму "Для кого самокат"')
    def fill_first_step_form_order(self):
        self.insert_input_firstname()
        self.insert_input_lastname()
        self.insert_input_address()
        self.insert_input_metro()
        self.insert_input_phone()

    @allure.step('Нажимаем "Далее"')
    def click_go_next(self):
        return self.click_on_element(OrderPageLocators.GO_NEXT)

    @allure.step('Ждем зарузки следующего шага')
    def wait_next_step_order_page(self):
        return self.find_element_with_wait(OrderPageLocators.INPUT_DATE_DELIVERY)

    @allure.step('Заполняем поле "Когда привезди самокат"')
    def insert_input_date_delivery(self):
        self.click_on_element(OrderPageLocators.INPUT_DATE_DELIVERY)
        return self.click_on_element(OrderPageLocators.DATE_DELIVERY)

    @allure.step('Заполняем поле "Срок аренды"')
    def insert_input_time_rental(self):
        self.click_on_element(OrderPageLocators.SELECT_TIME_RENTAL)
        return self.click_on_element(OrderPageLocators.TIME_RENTAL)

    @allure.step('Выбираем цвет самоката')
    def choose_scooter_colour(self):
        return self.click_on_element(OrderPageLocators.INPUT_COLOUR)

    @allure.step('Заполняем поле "Комментарий для курьера"')
    def insert_input_comment(self):
        return self.send_element(OrderPageLocators.INPUT_COMMENT, 'Комментарий')

    @allure.story('Запоняем форму "Про аренду"')
    def fill_second_step_form_order(self):
        self.insert_input_date_delivery()
        self.insert_input_time_rental()
        self.choose_scooter_colour()
        self.insert_input_comment()

    @allure.step('Нажимаем "Заказать" в форме заказа')
    def click_order_button_on_order_form_page(self):
        return self.click_on_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Ждем появления окна подтверждения')
    def wait_confirm_window_order(self):
        return self.find_element_with_wait(OrderPageLocators.CONFIRM_WINDOW_ORDER)

    @allure.step('Нажимаем "Да"')
    def click_yes_button(self):
        return self.click_on_element(OrderPageLocators.BUTTON_YES)

    @allure.step('Ждем появления окна успешного создания заказа')
    def wait_success_window_order(self):
        return self.find_element_with_wait(OrderPageLocators.SUCCESS_WINDOW_ORDER)

    @allure.step('Нажимаем "Посмотреть статус"')
    def click_сheck_status(self):
        return self.click_on_element(OrderPageLocators.BUTTON_CHECK_STATUS)


    @allure.step('Нажимаем на логотип "Яндекс" в шапке сайта')
    def click_to_yandex_in_header(self):
        return self.click_on_element(OrderPageLocators.HEADER_BUTTON_YANDEX)

    @allure.step('Ждем редиректа на страницу "Дзен"')
    def check_redirect_to_dzen(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return WebDriverWait(self.driver, 15).until(
            expected_conditions.url_contains("dzen.ru/?yredirect=true"))

    @allure.step('Нажимаем на логотип "Самокат" в шапке сайта')
    def click_scooter_on_header(self):
        return self.click_on_element(OrderPageLocators.HEADER_BUTTON_SCOOTER)

    @allure.step('Ждем открытия главное страницы "СамокатЯндекс"')
    def check_main_url_scooter_page(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.url_contains("qa-scooter.praktikum-services"))

