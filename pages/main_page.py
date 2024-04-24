import allure

import data
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Нажимаем на кнопку Конструктор")
    def click_constructor(self):
        locators = MainPageLocators
        self.click_to_element(*locators.button_constructors)

    @allure.step("Проверяем переход в меню Констируктора")
    def check_constructor(self):
        locators = MainPageLocators
        self.wait(*locators.text_main)
        assert self.get_text_from_element(*locators.text_main) == "Соберите бургер"

    @allure.step("Нажимаем на кнопку Лента заказов")
    def click_orders(self):
        locators = MainPageLocators
        self.click_to_element(*locators.orders)

    @allure.step("Проверяем переход в меню Лента заказов")
    def check_orders(self):
        locators = MainPageLocators
        self.wait(*locators.text_main)
        assert self.get_text_from_element(*locators.text_main) == "Лента заказов"

    @allure.step("Нажимаем на ингредиент")
    def click_ingredient(self):
        locators = MainPageLocators
        self.click_to_element(*locators.ingredient)

    @allure.step("Проверяем открытие вспывающего окна с ингредиентом")
    def check_ingredient(self):
        locators = MainPageLocators
        self.wait(*locators.details_ingredient)
        assert self.get_text_from_element(*locators.details_ingredient) == "Детали ингредиента"

    @allure.step("Нажимаем на закрытие окна с ингредиентами")
    def click_close_ingredient(self):
        locators = MainPageLocators
        self.click_to_element(*locators.button_close_ingredient)

    @allure.step("Проверяем закрытие вспывающего окна с ингредиентом")
    def check_close_window(self):
        locators = MainPageLocators
        self.wait(*locators.details_ingredient)
        assert len(self.find_element_and_wait(*locators.modaL_close)) > 0

    @allure.step("Перетаскивание ингредиента в заказ")
    def drag_and_drop_ingredients(self):
        locators = MainPageLocators
        self.wait(*locators.ingredient)
        ingredient = self.find_element_and_wait(*locators.ingredient)
        basket = self.find_element_and_wait(*locators.order_basket)
        self.drag_and_drop(ingredient, basket)

    @allure.step("Проверка увеличения счетчика")
    def check_adding_ingredient(self):
        locators = MainPageLocators
        assert int(self.get_text_from_element(*locators.count_ingredient)) == 2

    @allure.step("Авторизация пользователя")
    def authorization(self):
        locators = MainPageLocators
        self.click_to_element(*locators.entrance_button)
        self.send_text_to_element(*locators.authorization_email, data.email)
        self.send_text_to_element(*locators.authorization_password, data.password)
        self.click_to_element(*locators.button_authorization)

    @allure.step("Нажимаем на оформление заказа")
    def click_click_checkout(self):
        locators = MainPageLocators
        self.click_to_element(*locators.checkout)

    @allure.step("Проверка оформления заказа")
    def check_adding_ingredient(self):
        locators = MainPageLocators
        assert self.find_element_and_wait(*locators.name_order)

