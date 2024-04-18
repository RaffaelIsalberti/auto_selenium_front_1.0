from selenium.webdriver.common.by import By
import conftest


class LoginPage():

    def __init__(self):
        self.driver = conftest.driver
        self.field_users = (By.XPATH, "//a[@class='ico-login']")
        self.username_field = (By.XPATH, "//input[@class='email']")
        self.password_field = (By.XPATH, "//input[@class='password']")
        self.login_button = (By.XPATH, "//button[text()= 'Log in']")

    ##LOGIN -- melhorar com base page
    def fazer_login(self, usuario, senha):
        self.driver.find_element(*self.field_users).click()
        self.driver.find_element(*self.username_field).send_keys(usuario)
        self.driver.find_element(*self.password_field).send_keys(senha)
        self.driver.find_element(*self.login_button).click()
