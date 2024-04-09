import time

import pytest
import conftest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup_teardown")
class TestCT0003:
    def test_ct0003_loja_valido(self):
        driver = conftest.driver
        wait = WebDriverWait(driver, 5)

        ##LOGIN
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        ##User e senha
        driver.find_element(By.XPATH, "//input[@class='email']").send_keys('testeraffaelial@gmail.com')
        driver.find_element(By.XPATH, "//input[@class='password']").send_keys('Teste123@')
        driver.find_element(By.XPATH, "//button[text() ='Log in']").click()

        #ACTION EM VARIAVEL
        actions = ActionChains(driver)

        ##FUNÇÃO MOUSE HOVER - MOUSE FLUTUANTE
        mouse_tracker = driver.find_element(By.XPATH, "//a[text() ='Computers ']")
        actions.move_to_element(mouse_tracker).perform()
        desk_tracker = driver.find_element(By.XPATH, "//a[text() ='Desktops ']")
        actions.move_to_element(desk_tracker).perform()
        note_tracker = driver.find_element(By.XPATH, "//a[text() ='Notebooks ']")
        actions.move_to_element(note_tracker).perform()

        ##NAVEGAÇÃO LOJA NOTEBOOK
        driver.find_element(By.XPATH, "//a[text() ='Notebooks ']").click()
        produto0 = driver.find_element(By.ID, 'attribute-option-7')
        actions.click(produto0).perform()
        time.sleep(2)
        produto1 = driver.find_element(By.XPATH, "//h2/a[text() = 'Asus N551JK-XO076H Laptop']")
        #produto1 = wait.until(EC.presence_of_element_located((By.XPATH, "//h2/a[text() = 'HP Envy 6-1180ca 15.6-Inch Sleekbook']")))
        actions.click(produto1).perform()


        ##FUNÇÃO DOUBLE CLICK MOUSE e SCROLL
        #limpar campo para preenchimento
        camp_valor = driver.find_element(By.ID, "product_enteredQuantity_5")
        actions.scroll_to_element(camp_valor).perform()
        actions.double_click(camp_valor).perform()
        camp_valor.send_keys(Keys.DELETE)

        ##ADICIONAR FUNÇÃO WAIT
        camp_valor.send_keys('2')
        driver.find_element(By.ID, "add-to-cart-button-5").click()


        ##CARRINHO
        assert driver.find_element(By.XPATH, "//p[text()= 'The product has been added to your ']").is_displayed()
        driver.find_element(By.XPATH, "//span[@class='close']").click()

        ##MOUSE HOPER CARRINHO
        shop_cart = driver.find_element(By.XPATH, "//span[text()= 'Shopping cart']")
        actions.scroll_to_element(shop_cart).perform()
        actions.move_to_element(shop_cart).perform()
        driver.find_element(By.XPATH, "//button[@class='button-1 cart-button']").click()
