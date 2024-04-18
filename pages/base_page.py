import conftest


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def find_elem(self, locator):
        return self.driver.find_element(*locator)

    def writer(self, locator, text):
        self.find_elem(locator).send_keys(text)

    def cliq(self, locator):
        self.find_elem(locator).click()
