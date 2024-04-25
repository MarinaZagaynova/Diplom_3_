import allure

import data
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Нажимаем на кнопку Лента заказов")
    def click_orders(self):
        self.click_to_element(OrderPageLocators.orders)

    @allure.step("Нажимаем на заказ")
    def click_order(self):
        self.click_to_element(OrderPageLocators.order)

    @allure.step("Проверяем открытие вспывающего окна с деталями заказа")
    def check_order(self):
        assert self.get_text_from_element(OrderPageLocators.order_detail) == 'Cостав'

    @allure.step("Авторизация пользователя")
    def authorization(self):
        self.click_to_element(OrderPageLocators.entrance_button)
        self.send_text_to_element(OrderPageLocators.authorization_email, data.email)
        self.send_text_to_element(OrderPageLocators.authorization_password, data.password)
        self.click_to_element(OrderPageLocators.button_authorization)

    @allure.step("Создание заказа")
    def make_order(self):
        self.authorization()
        self.wait(OrderPageLocators.ingredient)
        ingredient = self.find_element_and_wait(OrderPageLocators.ingredient)
        basket = self.find_element_and_wait(OrderPageLocators.order_basket)
        self.drag_and_drop(ingredient, basket)
        self.click_to_element(OrderPageLocators.checkout)

    @allure.step("Получаем номер заказа и закрываем окно")
    def get_number_order_and_close_window(self):
        number = self.get_text_from_element(OrderPageLocators.order_number)
        self.click_to_element(OrderPageLocators.button_close)
        return number

    @allure.step("Проверяем наличие заказа пользователя в Ленте и истории заказов")
    def check_order_in_the_list_orders(self, number):
        assert number in self.get_text_from_element(OrderPageLocators.order_feed)

    @allure.step("Переход в раздел История заказов")
    def go_to_history_order(self):
        self.click_to_element(OrderPageLocators.entrance_button)
        self.click_to_element(OrderPageLocators.history_order)

    @allure.step("Проверяем наличие заказа пользователя в Истории заказов")
    def check_order_in_the_history_orders(self, number):
        self.scroll_to_end_of_page()
        assert number in self.get_text_from_element(OrderPageLocators.order_history)

    @allure.step("Получаем количество заказов")
    def get_count_orders(self):
        count = self.get_text_from_element(OrderPageLocators.count_orders)
        return count

    @allure.step("Проверяем количество заказов")
    def check_count_orders(self, count):
        self.click_to_element(OrderPageLocators.button_close)
        self.click_orders()
        assert int(self.get_text_from_element(OrderPageLocators.count_orders)) == int(count) + 1

    @allure.step("Получаем количество заказов за сегодня")
    def get_count_orders_today(self):
        count = self.get_text_from_element(OrderPageLocators.count_orders)
        return count

    @allure.step("Проверяем количество заказов за сегодня")
    def check_count_orders(self, count):
        self.click_to_element(OrderPageLocators.button_close)
        self.click_orders()
        assert int(self.get_text_from_element(OrderPageLocators.count_order_today)) == int(count) + 1

    @allure.step("Проверяем наличие заказа в разделе В работе")
    def check_number_at_work(self, number):
        self.click_orders()
        assert int(self.get_text_from_element(OrderPageLocators.number_at_work)) == int(number)
