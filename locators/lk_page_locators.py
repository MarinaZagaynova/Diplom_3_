from selenium.webdriver.common.by import By


class LkPageLocators:
    entrance_button = [By.LINK_TEXT, "Личный Кабинет"]
    text_entrance = [By.XPATH, "//h2[.='Вход']"]
    authorization_email = [By.XPATH, ".//input[@name='name']"]
    authorization_password = [By.XPATH, ".//input[@name='Пароль']"]
    button_authorization = [By.XPATH, "//button[contains(text(), 'Войти')]"]
    history_order = [By.LINK_TEXT, "История заказов"]
    button_exit = (By.XPATH, ".//button[text()='Выход']")
