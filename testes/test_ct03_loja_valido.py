import time
import pytest
import conftest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
#@pytest.mark.skip
class TestCT0003:
    def test_ct0003_loja_valido(self):
        driver = conftest.driver

        ##LOGIN
        pag1_login = LoginPage()
        pag1_login.fazer_login('testeraffaelial@gmail.com', 'Teste123@')

        #ACTION EM VARIAVEL
        actions = ActionChains(driver)

        ##FUNÇÃO MOUSE HOVER - MOUSE FLUTUANTE
        comp_tracker = driver.find_element(By.XPATH, "//a[text() ='Computers ']")
        actions.move_to_element(comp_tracker).perform()
        desk_tracker = driver.find_element(By.XPATH, "//a[text() ='Desktops ']")
        actions.move_to_element(desk_tracker).perform()
        note_tracker = driver.find_element(By.XPATH, "//a[text() ='Notebooks ']")
        actions.move_to_element(note_tracker).perform()

        ##NAVEGAÇÃO LOJA NOTEBOOK
        actions.click(note_tracker).perform()
        #driver.find_element(By.XPATH, "//a[text() ='Notebooks ']").click()
        product0 = driver.find_element(By.ID, 'attribute-option-7')
        actions.click(product0).perform()
        time.sleep(2)
        product1 = driver.find_element(By.XPATH, "//h2/a[text() = 'Asus N551JK-XO076H Laptop']")
        actions.click(product1).perform()


        ##FUNÇÃO DOUBLE CLICK MOUSE e SCROLL
        #limpar campo de quantidade para preenchimento
        camp_valor = driver.find_element(By.ID, "product_enteredQuantity_5")
        actions.scroll_to_element(camp_valor).perform()
        actions.double_click(camp_valor).perform()
        camp_valor.send_keys(Keys.DELETE)
        camp_valor.send_keys('2')

        ##ADICIONAR ITEM
        driver.find_element(By.ID, "add-to-cart-button-5").click()

        ##FECHAR MENSAGEM
        assert driver.find_element(By.XPATH, "//p[text()= 'The product has been added to your ']").is_displayed()
        driver.find_element(By.XPATH, "//span[@class='close']").click()

        ##MOUSE HOPER CARRINHO
        shop_cart = driver.find_element(By.XPATH, "//span[text()= 'Shopping cart']")
        actions.scroll_to_element(shop_cart).perform()
        actions.move_to_element(shop_cart).perform()
        driver.find_element(By.XPATH, "//button[@class='button-1 cart-button']").click()
        #assert driver.find_element(By.XPATH, "//h1[text() = 'Shopping cart']").is_displayed()

        ##MOUSE HOPER LOJA ELETRONICOS
        eletroni_tracker = driver.find_element(By.XPATH, "//ul[1]/li[2]/a[text()='Electronics ']")
        actions.move_to_element(eletroni_tracker).perform()
        cell_tracker = driver.find_element(By.XPATH, "//div[2]/ul[1]/li[2]/ul/li[2]/a[text()='Cell phones ']")
        actions.move_to_element(cell_tracker).perform()
        actions.click(cell_tracker).perform()
        product2 = driver.find_element(By.XPATH, "//h2/a[text()='Nokia Lumia 1020']")
        actions.click(product2).perform()

        ##ADICIONAR ITEM
        driver.find_element(By.ID, "add-to-cart-button-20").click()


        ##FECHAR MENSAGEM
        assert driver.find_element(By.XPATH, "//p[text()= 'The product has been added to your ']").is_displayed()
        driver.find_element(By.XPATH, "//span[@class='close']").click()
        shop_cart2 = driver.find_element(By.XPATH, "//span[text()= 'Shopping cart']")
        actions.scroll_to_element(shop_cart2).perform()
        actions.move_to_element(shop_cart2).perform()
        driver.find_element(By.XPATH, "//button[@class='button-1 cart-button']").click()

        #ESTIMAR ENVIO
        env_fret = driver.find_element(By.ID, "open-estimate-shipping-popup")
        actions.scroll_to_element(env_fret).perform()
        actions.move_to_element(env_fret).perform()
        actions.click(env_fret).perform()
        time.sleep(2)

        driver.find_element(By.ID, "CountryId").click()
        driver.find_element(By.XPATH, "//option[text()='Brazil']").click()
        time.sleep(3)
        #sel_country = driver.find_element(By.XPATH, "//option[text()='Brazil']")
        #actions.scroll_to_element(sel_country).perform()
        #actions.click(sel_country).perform()

