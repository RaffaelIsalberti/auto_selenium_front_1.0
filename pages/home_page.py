from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.valid_home = (By.XPATH, "// h2[text() = 'Welcome to our store']")

    def valid_home_pag(self):
        self.disp_valid(self.valid_home)

