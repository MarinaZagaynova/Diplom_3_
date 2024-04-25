from selenium.webdriver.common.by import By


class LkPageLocators:
    entrance_button = [By.CLASS_NAME, "button_button__33qZ0"]
    button_recover = [By.XPATH, "//a[contains(text(),'Восстановить пароль')]"]
    email_input = [By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//input[@name='name']"]
    recover = [By.XPATH, "//button[contains(text(),'Восстановить')]"]