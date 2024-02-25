import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def driver():
    fox_driver = GeckoDriverManager().install()
    service = Service(fox_driver)
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()
