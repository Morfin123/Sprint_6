import allure


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Открываем главную страницу "Яндекс Самокат"')
    def open_scooter_main_page(self):
        return self.driver.get(self.url)