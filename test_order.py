import data
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from datetime import date

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


class TestTest:
    HEADER_BUTTON_ORDER = [By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]']
    PAGE_BUTTON_ORDER = [By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']

    INPUT_FIRST_NAME = [By.XPATH, '//input[@placeholder="* Имя"]']
    INPUT_LAST_NAME = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    INPUT_DELIVERY_ADDRESS = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    INPUT_METRO = [By.XPATH, '//input[@placeholder="* Станция метро"]']
    INPUT_PHONE = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']

    METRO = [By.XPATH, f'//li[@data-value="{get_random_metro()}"]']

    GO_NEXT = [By.XPATH, '//button[text()="Далее"]']

    INPUT_DATE_DELIVERY = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    DATE_DELIVERY = [By.XPATH, f'//div[@class="react-datepicker__month"]//div[text()="{date.today().day}"]']

    SELECT_TIME_RENTAL = [By.XPATH, '//div[text()="* Срок аренды"]']
    TIME_RENTAL = [By.XPATH, f'//div[text()="{get_random_time_rental()}"]']

    INPUT_COLOUR = [By.ID, f'{get_random_colour()}']

    INPUT_COMMENT = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']

    BUTTON_ORDER = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']

    BUTTON_YES = [By.XPATH, '//button[text()="Да"]']

    BUTTON_CHECK_STATUS = [By.XPATH, '//button[text()="Посмотреть статус"]']

    BUTTON_CANCEL_ORDER = [By.XPATH, '//button[text()="Отменить заказ"]']

    HEADER_BUTTON_YANDEX = [By.XPATH, '//img[@alt="Yandex"]']

    HEADER_BUTTON_SCOOTER = [By.XPATH, '//img[@alt="Scooter"]']
    def test_test(self):
        fox_driver = GeckoDriverManager().install()
        service = Service(fox_driver)
        driver = webdriver.Firefox(service=service)
        driver.get(data.BASE_URL)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (self.HEADER_BUTTON_ORDER))).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (self.INPUT_FIRST_NAME))).send_keys('Имя')

        driver.find_element(*self.INPUT_LAST_NAME).send_keys('Фамилия')

        driver.find_element(*self.INPUT_DELIVERY_ADDRESS).send_keys('Пушкина')

        driver.find_element(*self.INPUT_METRO).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (self.METRO))).click()

        driver.find_element(*self.INPUT_PHONE).send_keys(get_random_phone())

        driver.find_element(*self.GO_NEXT).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (self.INPUT_DATE_DELIVERY))).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (self.DATE_DELIVERY))).click()

        driver.find_element(*self.SELECT_TIME_RENTAL).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (self.TIME_RENTAL))).click()

        driver.find_element(*self.INPUT_COLOUR).click()

        driver.find_element(*self.INPUT_COMMENT).send_keys('Комментарий')

        driver.find_element(*self.BUTTON_ORDER).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (self.BUTTON_YES))).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (self.BUTTON_CHECK_STATUS))).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (self.BUTTON_CANCEL_ORDER)))

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (self.HEADER_BUTTON_YANDEX))).click()


        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 15).until(expected_conditions.url_contains("dzen.ru/?yredirect=true"))
        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (self.HEADER_BUTTON_SCOOTER))).click()

        WebDriverWait(driver, 30).until(expected_conditions.url_contains("qa-scooter.praktikum-services"))



