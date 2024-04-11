from selenium.webdriver.common.by import By
import conftest

class LoginPage:
    def __init__(self): ##construtor da classes
        self.driver = conftest.driver
    ##LOGIN
    def fazer_login(self, usuario, senha):
        self.driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        self.driver.find_element(By.XPATH, "//input[@class='email']").send_keys(usuario)
        self.driver.find_element(By.XPATH, "//input[@class='password']").send_keys(senha)
        self.driver.find_element(By.XPATH, "//button[text()= 'Log in']").click()

