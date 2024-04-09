import pytest
import conftest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.skip
class TestCT00000:
    def test_ct0000_login_inval(self):
        driver = conftest.driver
        ##LOGIN
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        ##User e senha
        driver.find_element(By.XPATH, "//input[@class='email']").send_keys('testeraffaelial@gmail.com')
        driver.find_element(By.XPATH, "//input[@class='password']").send_keys('Tesxxxxx@')
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

