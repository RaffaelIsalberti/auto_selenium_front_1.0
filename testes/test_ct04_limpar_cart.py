import pytest
import conftest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.skip
class TestCT0004:
    def test_ct0004_limp_cart(self):
        driver = conftest.driver

        ##LOGIN
        pag2_login = LoginPage()
        pag2_login.fazer_login("testeraffaelial@gmail.com", "Teste123@")

        ##FUNÇÃO MOUSE HOVER - MOUSE FLUTUANTE
        actions = ActionChains(driver)
        shop_car = driver.find_element(By.XPATH, "//span[text()= 'Shopping cart']")
        actions.move_to_element(shop_car).perform()
        driver.find_element(By.XPATH, "//button[@class='button-1 cart-button']").click()

        #LIMPAR CARRINHO
        clean_shop = driver.find_element(By.XPATH, "//button[@class='remove-btn']")
        actions.click(clean_shop).perform()
        clean_shop1 = driver.find_element(By.XPATH, "//button[@class='remove-btn']")
        actions.click(clean_shop1).perform()

        log_out = driver.find_element(By.XPATH, "//a[text() = 'Log out']")
        actions.click(log_out).perform()
        assert driver.find_element(By.XPATH, "//h2[text()= 'Welcome to our store']").is_displayed()

        driver.quit()
