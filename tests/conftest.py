import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
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