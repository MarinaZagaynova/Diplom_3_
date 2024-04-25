import allure


@allure.suite('Личный кабинет')
class TestLkPage:

    @allure.title('Тест перехода в Личный кабинет, перехода в раздел История заказов и Выход')
    def test_check_lk_and_history_orders_and_logout(self, lk_page):
        lk_page.button_login_click()
        lk_page.check_login()
        lk_page.authorization()
        lk_page.button_order_click()
        lk_page.check_history_orders()
        lk_page.button_exit_click()
        lk_page.check_exit()



