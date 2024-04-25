import pytest
from selenium import webdriver

import data
from pages.lk_page import LkPage
from pages.order_page import OrderPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.main_page import MainPage


@pytest.fixture(params=['chrome'])
def webpage(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    url = data.DataUrl.URL
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(webpage):
    main_page = MainPage(webpage)
    return main_page


@pytest.fixture(scope='function')
def password_recovery_page(webpage):
    password_recovery_page = PasswordRecoveryPage(webpage)
    return password_recovery_page


@pytest.fixture(scope='function')
def order_page(webpage):
    order_page = OrderPage(webpage)
    return order_page


@pytest.fixture(scope='function')
def lk_page(webpage):
    lk_page = LkPage(webpage)
    return lk_page
