import conftest


class BasePage():
    def __init__(self):
        self.driver = conftest.driver

    def find_hele(self, locator):
        return self.driver.find_element(*locator)

    def writer(self, locator, text):
        self.find_hele(locator).send_keys(text)

    def cliq(self, locator):
        self.find_hele(locator).click()

    def disp_valid(self, locator):
        assert self.find_hele(locator).is_displayed()
