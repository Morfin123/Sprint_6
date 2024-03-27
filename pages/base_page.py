import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        return self.driver.get(self.url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def scroll_to_element(self, locator):
        return self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def send_element(self, locator, value):
        element = self.find_element_with_wait(locator)
        element.send_keys(value)

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)



