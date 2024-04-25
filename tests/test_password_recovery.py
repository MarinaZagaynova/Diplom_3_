import allure


@allure.suite('Тест Восстановление пароля')
class TestPasswordRecover:

    @allure.title('Тест восстановления пароля')
    @allure.description('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль», ввод почты и клик '
                        'по кнопке Восстановить. Клик по кнопке показать/скрыть пароль делает поле активным -'
                        'подсвечивает его.')
    def test_password_recover(self, password_recovery_page):
        password_recovery_page.button_login_click()
        password_recovery_page.button_recover_click()
        password_recovery_page.check_recover()
        password_recovery_page.send_email_and_button_recover_click()
        password_recovery_page.check_password_recover()
        password_recovery_page.check_eye_button()



