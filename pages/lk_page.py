import allure

import data
from locators.lk_page_locators import LkPageLocators
from pages.base_page import BasePage


class LkPage(BasePage):
    @allure.step("Переход на страницу авторизации по клику на Личный кабинет")
    def button_login_click(self):
        self.click_to_element(LkPageLocators.entrance_button)

    @allure.step("Проверка нахождения на странице авторизации")
    def check_login(self):
        assert self.get_text_from_element(LkPageLocators.text_entrance) == 'Вход'

    @allure.step("Авторизация пользователя")
    def authorization(self):
        self.send_text_to_element(LkPageLocators.authorization_email, data.email)
        self.send_text_to_element(LkPageLocators.authorization_password, data.password)
        self.click_to_element(LkPageLocators.button_authorization)

    @allure.step("Переход на страницу История заказов")
    def button_order_click(self):
        self.click_to_element(LkPageLocators.entrance_button)
        self.click_to_element(LkPageLocators.history_order)

    @allure.step("Проверка нахождения на странице История заказов")
    def check_history_orders(self):
        assert self.get_redirected_url() == data.DataUrl.URL + data.DataUrl.HISTORY

    @allure.step("Выход")
    def button_exit_click(self):
        self.click_to_element(LkPageLocators.button_exit)

    @allure.step("Проверка нахождения на странице выхода")
    def check_exit(self):
        self.wait(LkPageLocators.text_entrance)
        assert self.get_redirected_url() == data.DataUrl.URL + data.DataUrl.LOGIN

