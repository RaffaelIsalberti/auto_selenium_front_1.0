from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import conftest


class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        self.driver = conftest.driver
        self.field_users = (By.XPATH, "//a[@class='ico-login']")
        self.username_field = (By.XPATH, "//input[@class='email']")
        self.password_field = (By.XPATH, "//input[@class='password']")
        self.login_button = (By.XPATH, "//button[text()= 'Log in']")

    ##LOGIN -- melhorar com base page
    def fazer_login(self, usuario, senha):
        self.cliq(self.field_users)
        self.writer(self.username_field, usuario)
        self.writer(self.password_field, senha)
        self.cliq(self.login_button)
