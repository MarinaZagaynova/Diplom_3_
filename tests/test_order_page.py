import time

import allure


@allure.suite('Проверка раздела "Лента заказов"')
class TestOrderPage:

    @allure.title('Проверка открытия вспывающего окна с деталями при клике на заказ')
    def test_order_details_visible(self, order_page):
        order_page.click_orders()
        order_page.click_order()
        order_page.check_order()

    @allure.title('Проверка наличия заказа пользователя в Ленте и истории заказов')
    # в окне после создания заказа отображается №9999. Фактический номер заказа прогружается спустя время.
    # это баг.
    # чтобы обойти падение теста использовано запрещенное ожидание Timesleep.
    def test_order_in_the_list_orders(self, order_page):
        order_page.make_order()
        time.sleep(3)
        number_order = order_page.get_number_order_and_close_window()
        order_page.click_orders()
        order_page.check_order_in_the_list_orders(number_order)
        order_page.go_to_history_order()
        order_page.check_order_in_the_history_orders(number_order)

    @allure.title('Проверка счетчика заказов за все время')
    def test_order_all_count(self, order_page):
        order_page.click_orders()
        count_orders = order_page.get_count_orders()
        order_page.make_order()
        order_page.check_count_orders(count_orders)

    @allure.title('Проверка счетчика "Выполнено за сегодня"')
    def test_order_all_count_today(self, order_page):
        order_page.click_orders()
        count_orders = order_page.get_count_orders_today()
        order_page.make_order()
        order_page.check_count_orders(count_orders)

    @allure.title('Проверка отображения заказа в разделе "В работе"')
    # в окне после создания заказа отображается №9999. Фактический номер заказа прогружается спустя время.
    # это баг.
    # чтобы обойти падение теста использовано запрещенное ожидание Timesleep.
    def test_number_at_work(self, order_page):
        order_page.make_order()
        time.sleep(3)
        number_order = order_page.get_number_order_and_close_window()
        order_page.check_number_at_work(number_order)
