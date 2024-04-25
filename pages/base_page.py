from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def find_element_and_wait(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def send_text_to_element(self, locator, text):
        self.find_element_and_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_and_wait(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    def switch_to_page(self, locator):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait(locator)
        redirected_url = self.driver.current_url
        return redirected_url

    def wait(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))

    def drag_and_drop(self, locator_one, locator_two):
        ActionChains(self.driver).drag_and_drop(locator_one, locator_two).perform()

    def get_attribute_class_of_element(self, locator):
        return self.find_element_and_wait(locator).get_attribute("class")
