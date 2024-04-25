import allure

from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    @allure.step("Переход на страницу авторизации")
    def button_login_click(self):
        self.click_to_element(PasswordRecoveryPageLocators.entrance_button)

    @allure.step("Переход на страницу восстановления пароля")
    def button_recover_click(self):
        self.click_to_element(PasswordRecoveryPageLocators.button_recover)

    @allure.step("Проверка нахождения на странице восстановления пароля")
    def check_recover(self):
        assert self.get_text_from_element(PasswordRecoveryPageLocators.check_title) == "Восстановление пароля"

    @allure.step("Ввод почты и нажать на Восстановить пароль")
    def send_email_and_button_recover_click(self):
        self.send_text_to_element(PasswordRecoveryPageLocators.email_input, "email@email.com")
        self.click_to_element(PasswordRecoveryPageLocators.recover)

    @allure.step("Проверка нахождения на странице восстановления пароля")
    def check_password_recover(self):
        assert self.find_element_and_wait(PasswordRecoveryPageLocators.password_input)

    @allure.step("Проверка кнопки показать/скрыть пароль")
    def check_eye_button(self):
        self.click_to_element(PasswordRecoveryPageLocators.button_eye)
        assert "input__placeholder-focused" in self.get_attribute_class_of_element(PasswordRecoveryPageLocators.input_before_click)

