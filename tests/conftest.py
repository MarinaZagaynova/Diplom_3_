import pytest
from selenium import webdriver

from pages.main_page import MainPage


@pytest.fixture(params=['chrome'])
def webpage(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    url = 'https://stellarburgers.nomoreparties.site'
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(webpage):
    main_page = MainPage(webpage)
    return main_page




@pytest.fixture(scope='function')
def order_page(webpage):
    order_page = OrderPage(webpage)
    return order_page


@pytest.fixture(scope='function')
def lk_page(webpage):
    lk_page = LK(webpage)
    return lk_page