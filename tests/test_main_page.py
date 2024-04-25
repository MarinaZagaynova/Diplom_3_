import allure


@allure.suite('Проверка основного функционала')
class TestMainFunctionality:

    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_click_constructor(self, main_page):
        main_page.click_constructor()
        main_page.check_constructor()

    @allure.title('Проверка перехода по клику на  "Лента заказов"')
    def test_click_orders(self, main_page):
        main_page.click_orders()
        main_page.check_orders()

    @allure.title('Проверка открытия вспывающего окна при клике на ингредиент')
    def test_click_ingredient(self, main_page):
        main_page.click_ingredient()
        main_page.check_ingredient()

    @allure.title('Проверка закрытия окна с деталями ингредиента')
    def test_window_with_ingredient_clos(self, main_page):
        main_page.click_ingredient()
        main_page.click_close_ingredient()
        main_page.check_close_window()

    @allure.title('Проверка работы счетчика ингредиента заказа')
    def test_check_adding_ingredient(self, main_page):
        main_page.drag_and_drop_ingredients()
        main_page.check_adding_ingredient()

    @allure.title('Проверка оформления заказа')
    def test_user_make_order(self, main_page):
        main_page.authorization()
        main_page.drag_and_drop_ingredients()
        main_page.click_checkout()
        main_page.check_order()
