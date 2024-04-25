from selenium.webdriver.common.by import By


class OrderPageLocators:
    orders = [By.LINK_TEXT, "Лента Заказов"]
    order = [By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li[2]"]
    order_detail = (By.XPATH, "//p[contains(text(),'Cостав')]")
    entrance_button = [By.LINK_TEXT, "Личный Кабинет"]
    authorization_email = [By.XPATH, ".//input[@name='name']"]
    authorization_password = [By.XPATH, ".//input[@name='Пароль']"]
    button_authorization = [By.XPATH, "//button[contains(text(), 'Войти')]"]
    ingredient = [By.XPATH, "//p[text() ='Флюоресцентная булка R2-D3']"]
    order_basket = [By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']"]
    checkout = [By.XPATH, ".//button[text()='Оформить заказ']"]
    order_number = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__')]")
    button_close = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close_modified__')]")
    order_feed = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list__')]")
    order_history = (By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList__374GU')]")
    history_order = [By.LINK_TEXT, "История заказов"]
    count_orders = (By.XPATH, ".//p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']")
    count_order_today = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__')]")
    number_at_work = (By.XPATH, ".//li[@class = 'text text_type_digits-default mb-2']")