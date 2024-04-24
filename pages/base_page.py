from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

import conftest


class BasePage:
    def __init__(self):
        self.driver = conftest.driver
        self.actions = ActionChains(self.driver)

    def find_hele(self, locator):
        return self.driver.find_element(*locator)

    def writer(self, locator, text):
        self.find_hele(locator).send_keys(text)

    def cliq(self, locator):
        self.find_hele(locator).click()

    def disp_valid(self, locator):
        assert self.find_hele(locator).is_displayed()

    def move_to_element(self, locator):
        element = self.find_hele(locator)
        self.actions.move_to_element(element).perform()

    def wait_to_element(self, function, timeout=10):
        def condition(driver):
            try:
                function()
                return True
            except Exception:
                return False
        WebDriverWait(self.driver, timeout).until(condition)
