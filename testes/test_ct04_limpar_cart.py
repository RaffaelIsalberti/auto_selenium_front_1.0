import pytest
import conftest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
#@pytest.mark.skip
class TestCT0004:
    def test_ct0004_limp_cart(self):

        driver = conftest.driver

        ##LOGIN
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        driver.find_element(By.XPATH, "//input[@class='email']").send_keys('testeraffaelial@gmail.com')
        driver.find_element(By.XPATH, "//input[@class='password']").send_keys('Teste123@')
        driver.find_element(By.XPATH, "//button[text() ='Log in']").click()


        ##FUNÇÃO MOUSE HOVER - MOUSE FLUTUANTE
        actions = ActionChains(driver)
        shop_car = driver.find_element(By.XPATH, "//span[text()= 'Shopping cart']")
        actions.move_to_element(shop_car).perform()
        driver.find_element(By.XPATH, "//button[@class='button-1 cart-button']").click()

        #LIMPAR CARRINHO
        limpar_compra = driver.find_element(By.XPATH, "//button[@class='remove-btn']")
        actions.click(limpar_compra).perform()

        log_out = driver.find_element(By.XPATH, "//a[text() = 'Log out']")
        actions.click(log_out).perform()
        assert driver.find_element(By.XPATH, "//h2[text()= 'Welcome to our store']").is_displayed()

        driver.quit()
