import allure
import data
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
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
    METRO = [By.XPATH, f'//li[@data-value="{data.DataOrderPage.get_random_metro()}"]']
    GO_NEXT = [By.XPATH, '//button[text()="Далее"]']
    INPUT_DATE_DELIVERY = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    DATE_DELIVERY = [By.XPATH, f'//div[@class="react-datepicker__month"]//div[text()="{date.today().day}"]']
    SELECT_TIME_RENTAL = [By.XPATH, '//div[text()="* Срок аренды"]']
    TIME_RENTAL = [By.XPATH, f'//div[text()="{data.DataOrderPage.get_random_time_rental()}"]']
    INPUT_COLOUR = [By.ID, f'{data.DataOrderPage.get_random_colour()}']
    INPUT_COMMENT = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']
    BUTTON_ORDER = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']
    CONFIRM_WINDOW_ORDER = [By.CLASS_NAME, 'Order_Modal__YZ-d3']
    BUTTON_YES = [By.XPATH, '//button[text()="Да"]']
    SUCCESS_WINDOW_ORDER = [By.XPATH, '//div[text()="Заказ оформлен"]']
    BUTTON_CHECK_STATUS = [By.XPATH, '//button[text()="Посмотреть статус"]']
    BUTTON_CANCEL_ORDER = [By.XPATH, '//button[text()="Отменить заказ"]']
    HEADER_BUTTON_YANDEX = [By.XPATH, '//img[@alt="Yandex"]']
    HEADER_BUTTON_SCOOTER = [By.XPATH, '//img[@alt="Scooter"]']


class OrderPageHelper(BasePage):
    @allure.step('Открываем главную страницу "Яндекс Самокат"')
    def open_scooter_main_page(self):
        return self.driver.get(self.url)

    @allure.step('Ждем загрузку главной страницы')
    def wait_open_page(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((OrderPageLocators.MAIN_PAGE_LOGO)))
    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_order_button(self, order_button):
        return self.driver.find_element(*order_button).click()

    @allure.step('Ждем загрузку страницы оформления заказа')
    def wait_open_order_page(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((OrderPageLocators.INPUT_FIRST_NAME)))
    @allure.step('Заполняем поле "Имя"')
    def insert_input_firstname(self):
        return self.driver.find_element(*OrderPageLocators.INPUT_FIRST_NAME).send_keys('Имя')

    @allure.step('Заполняем поле "Фамилия"')
    def insert_input_lastname(self):
        return self.driver.find_element(*OrderPageLocators.INPUT_LAST_NAME).send_keys('Фамилия')

    @allure.step('Заполняем поле "Адрес"')
    def insert_input_address(self):
        return self.driver.find_element(*OrderPageLocators.INPUT_DELIVERY_ADDRESS).send_keys('Пушкина')

    @allure.step('Заполняем поле "Станция метро"')
    def insert_input_metro(self):
        self.driver.find_element(*OrderPageLocators.INPUT_METRO).click()
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((OrderPageLocators.METRO))).click()

    @allure.step('Заполняем поле "Телефон"')
    def insert_input_phone(self):
        return self.driver.find_element(*OrderPageLocators.INPUT_PHONE).send_keys(
            data.DataOrderPage.get_random_phone())

    @allure.step('Нажимаем "Далее"')
    def click_go_next(self):
        return self.driver.find_element(*OrderPageLocators.GO_NEXT).click()

    @allure.step('Ждем зарузки следующего шага')
    def wait_next_step_order_page(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((OrderPageLocators.INPUT_DATE_DELIVERY)))

    @allure.step('Заполняем поле "Когда привезди самокат"')
    def insert_input_date_delivery(self):
        self.driver.find_element(*OrderPageLocators.INPUT_DATE_DELIVERY).click()
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((OrderPageLocators.DATE_DELIVERY))).click()

    @allure.step('Заполняем поле "Срок аренды"')
    def insert_input_time_rental(self):
        self.driver.find_element(*OrderPageLocators.SELECT_TIME_RENTAL).click()
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((OrderPageLocators.TIME_RENTAL))).click()

    @allure.step('Выбираем цвет самоката')
    def choose_scooter_colour(self):
        return self.driver.find_element(*OrderPageLocators.INPUT_COLOUR).click()

    @allure.step('Заполняем поле "Комментарий для курьера"')
    def insert_input_comment(self):
        return self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys('Комментарий')

    @allure.step('Нажимаем "Заказать"')
    def click_order_button(self):
        return self.driver.find_element(*OrderPageLocators.BUTTON_ORDER).click()

    @allure.step('Ждем появления окна подтверждения')
    def wait_confirm_window_order(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((OrderPageLocators.CONFIRM_WINDOW_ORDER)))

    @allure.step('Нажимаем "Да"')
    def click_yes_button(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((OrderPageLocators.BUTTON_YES))).click()

    @allure.step('Ждем появления окна успешного создания заказа')
    def wait_success_window_order(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((OrderPageLocators.SUCCESS_WINDOW_ORDER)))

    @allure.step('Нажимаем "Посмотреть статус"')
    def click_сheck_status(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((OrderPageLocators.BUTTON_CHECK_STATUS))).click()

    @allure.step('Ждем открытия страницы созданного заказа')
    def wait_open_created_order_page(self):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((OrderPageLocators.BUTTON_CANCEL_ORDER)))

    @allure.step('Нажимаем на логотип "Яндекс" в шапке сайта')
    def click_to_yandex_in_header(self):
        return self.driver.find_element(*OrderPageLocators.HEADER_BUTTON_YANDEX).click()

    @allure.step('Ждем редиректа на страницу "Дзен"')
    def check_redirect_to_dzen(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return WebDriverWait(self.driver, 15).until(
            expected_conditions.url_contains("dzen.ru/?yredirect=true"))

    @allure.step('Нажимаем на логотип "Самокат" в шапке сайта')
    def click_scooter_to_dzen(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((OrderPageLocators.HEADER_BUTTON_SCOOTER))).click()

    @allure.step('Ждем открытия главное страницы "СамокатЯндекс"')
    def check_main_url_scooter_page(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.url_contains("qa-scooter.praktikum-services"))
