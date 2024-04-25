from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    entrance_button = [By.CLASS_NAME, "button_button__33qZ0"]
    button_recover = [By.XPATH, "//a[contains(text(),'Восстановить пароль')]"]
    email_input = [By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//input[@name='name']"]
    recover = [By.XPATH, "//button[contains(text(),'Восстановить')]"]
    check_title = [By.XPATH, "//h2[.='Восстановление пароля']"]
    password_input = [By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//label[.='Пароль']"]
    button_eye = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]")
    input_before_click = (By.XPATH, ".//label[contains(@class, 'input__placeholder text noselect text_type_main-default')]")