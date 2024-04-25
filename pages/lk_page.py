import allure

import data
from locators.lk_page_locators import LkPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class LK(BasePage):
    @allure.step("Переход на страницу авторизации")
    def button_login_click(self):
        locators = LkPageLocators
        self.click_to_element(*locators.entrance_button)

    @allure.step("Переход на страницу восстановления пароля")
    def button_recover_click(self):
        locators = LkPageLocators
        self.click_to_element(*locators.button_recover)

    @allure.step("Ввод почты и нажать на Восстановить пароль")
    def button_recover_click(self):
        locators = LkPageLocators
        self.send_text_to_element(*locators.email_input, "email@email.com")
        self.click_to_element(*locators.recover)
