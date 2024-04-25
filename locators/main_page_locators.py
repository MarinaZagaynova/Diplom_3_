from selenium.webdriver.common.by import By


class MainPageLocators:
    button_constructors = [By.XPATH, ".//p[text()='Конструктор']"]
    text_main = [By.CLASS_NAME, "text_type_main-large"]
    text_order = [By.XPATH, "//h1[.='Лента заказов']"]
    orders = [By.LINK_TEXT, "Лента Заказов"]
    ingredient = [By.XPATH, "//p[text() ='Флюоресцентная булка R2-D3']"]
    details_ingredient = [By.XPATH, "//h2[text()='Детали ингредиента']"]
    button_close_ingredient = [By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__')]"]
    modaL_close = [By.CLASS_NAME, 'Modal_modal__P3_V5']
    order_basket = [By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']"]
    count_ingredient = [By.XPATH, ".//p[@class = 'counter_counter__num__3nue1']"]
    authorization_email = [By.XPATH, ".//input[@name='name']"]
    authorization_password = [By.XPATH, ".//input[@name='Пароль']"]
    button_authorization = [By.XPATH, "//button[contains(text(), 'Войти')]"]
    entrance_button = [By.CLASS_NAME, "button_button__33qZ0"]
    checkout = [By.XPATH, ".//button[text()='Оформить заказ']"]
    name_order = [By.XPATH, "//p[text()='идентификатор заказа']"]