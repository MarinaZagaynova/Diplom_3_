import allure

import data
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Нажимаем на кнопку Конструктор")
    def click_constructor(self):
        self.click_to_element(MainPageLocators.button_constructors)

    @allure.step("Проверяем переход в меню Констируктора")
    def check_constructor(self):
        assert self.get_text_from_element(MainPageLocators.text_main) == "Соберите бургер"

    @allure.step("Нажимаем на кнопку Лента заказов")
    def click_orders(self):
        self.click_to_element(MainPageLocators.orders)

    @allure.step("Проверяем переход в меню Лента заказов")
    def check_orders(self):
        self.wait(MainPageLocators.text_order)
        assert self.get_text_from_element(MainPageLocators.text_main) == "Лента заказов"

    @allure.step("Нажимаем на ингредиент")
    def click_ingredient(self):
        self.click_to_element(MainPageLocators.ingredient)

    @allure.step("Проверяем открытие вспывающего окна с ингредиентом")
    def check_ingredient(self):
        assert self.get_text_from_element(MainPageLocators.details_ingredient) == "Детали ингредиента"

    @allure.step("Нажимаем на закрытие окна с ингредиентами")
    def click_close_ingredient(self):
        self.click_to_element(MainPageLocators.button_close_ingredient)

    @allure.step("Проверяем закрытие вспывающего окна с ингредиентом")
    def check_close_window(self):
        assert 'Modal_modal_opened' not in self.get_attribute_class_of_element(MainPageLocators.modaL_close)

    @allure.step("Перетаскивание ингредиента в заказ")
    def drag_and_drop_ingredients(self):
        self.wait(MainPageLocators.ingredient)
        ingredient = self.find_element_and_wait(MainPageLocators.ingredient)
        basket = self.find_element_and_wait(MainPageLocators.order_basket)
        self.drag_and_drop(ingredient, basket)

    @allure.step("Проверка увеличения счетчика")
    def check_adding_ingredient(self):
        assert int(self.get_text_from_element(MainPageLocators.count_ingredient)) == 2

    @allure.step("Авторизация пользователя")
    def authorization(self):
        self.click_to_element(MainPageLocators.entrance_button)
        self.send_text_to_element(MainPageLocators.authorization_email, data.email)
        self.send_text_to_element(MainPageLocators.authorization_password, data.password)
        self.click_to_element(MainPageLocators.button_authorization)

    @allure.step("Нажимаем на оформление заказа")
    def click_checkout(self):
        self.click_to_element(MainPageLocators.checkout)

    @allure.step("Проверка оформления заказа")
    def check_order(self):
        assert self.find_element_and_wait(MainPageLocators.name_order)

