import pytest
import conftest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.skip
class TestCT001:
    def test_ct001_regist_valid(self):
        driver = conftest.driver
        ##Registro
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()

        ##Dados
        driver.find_element(By.ID, 'gender-male').click()
        firstname = driver.find_element(By.XPATH, "//input[@name='FirstName']")
        secondname = driver.find_element(By.XPATH, "//input[@name='LastName']")
        firstname.send_keys('TesteRaffa')
        secondname.send_keys('RaffaTeste')

        ##Data Nascimento
        driver.find_element(By.XPATH, "//select[@name='DateOfBirthDay']").click()
        driver.find_element(By.XPATH, "//option[@value='5']").click()
        driver.find_element(By.XPATH, "//select[@name='DateOfBirthMonth']").click()
        driver.find_element(By.XPATH, "//option[@value='4' and text()= 'April']").click()
        driver.find_element(By.XPATH, "//select[@name='DateOfBirthYear']").click()
        driver.find_element(By.XPATH, "//option[@value='2000']").click()

        ##Contato
        driver.find_element(By.ID, 'Email').send_keys('testeraffaelial@gmail.com')

        ##Empresa
        name_company = driver.find_element(By.ID, 'Company')
        name_company.send_keys('Teste Raffael LTDA')

        ##Senha
        password = driver.find_element(By.ID, 'Password')
        password.send_keys('Teste123@')
        password = driver.find_element(By.ID, 'ConfirmPassword')
        password.send_keys('Teste123@')

        ##Botão Registro
        driver.find_element(By.XPATH, "//button[@id='register-button']").click()
        confirm_register = driver.find_element(By.XPATH, "//div[@class='result']")

        print('Registro confirmado',confirm_register.is_displayed())
        assert confirm_register.is_displayed()
