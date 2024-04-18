from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.field_users = (By.XPATH, "//a[@class='ico-login']")
        self.username_field = (By.XPATH, "//input[@class='email']")
        self.password_field = (By.XPATH, "//input[@class='password']")
        self.login_button = (By.XPATH, "//button[text()= 'Log in']")

    ##LOGIN -- criar metodo mais eficaz e limpo com basepage
    def fazer_login(self, usuario, senha):
        self.cliq(self.field_users)
        self.writer(self.username_field, usuario)
        self.writer(self.password_field, senha)
        self.cliq(self.login_button)
