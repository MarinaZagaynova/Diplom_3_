import pytest
from selenium import webdriver

from pages.password_recovery_page import PasswordRecoveryPage
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
def password_recovery_page(webpage):
    password_recovery_page = PasswordRecoveryPage(webpage)
    return password_recovery_page
