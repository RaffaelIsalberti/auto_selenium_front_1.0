import time
import pytest
import conftest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
#@pytest.mark.skip
class TestCT0003:
    def test_ct0003_loja_valido(self):
        driver = conftest.driver
        pag_login = LoginPage()
        home_page = HomePage()

        ##LOGIN
        pag_login.fazer_login('testeraffaelial@gmail.com', 'Teste123@')

        # ACTION EM VARIAVEL
        actions = ActionChains(driver)

        ##FUNÇÃO MOUSE HOVER - MOUSE FLUTUANTE
        home_page.move_to_sessao()
        home_page.sel_opc_prod()

        ##NAVEGAÇÃO LOJA NOTEBOOK
        home_page.buy_product()
        # home_page.marca_opc()
        # time.sleep(2)
        # home_page.add_ao_cart()

        ##FUNÇÃO DOUBLE CLICK MOUSE e SCROLL
        #limpar campo de quantidade para preenchimento
        home_page.find_field_qtd()

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

        ##MOUSE HOPER LOJA ELETRONICOS
        home_page.shop_eletrc()
        # home_page.mover_ao_cart()
        # home_page.mover_ao_prod()
        # home_page.add_ao_cart2('Nokia Lumia 1020')

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
        time.sleep(2)
        env_fret = driver.find_element(By.ID, "open-estimate-shipping-popup")
        #actions.scroll_to_element(env_fret).perform()
        actions.move_to_element(env_fret).perform()
        actions.click(env_fret).perform()
        time.sleep(2)

        #FECHAR COMPRA
        driver.find_element(By.ID, "CountryId").click()
        driver.find_element(By.XPATH, "//option[text()='Brazil']").click()
        driver.find_element(By.ID, "ZipPostalCode").send_keys("38400040")
        driver.find_element(By.XPATH, "//div[@class='estimate-shipping-row-item shipping-item' and text() = 'Next Day Air']").click()
        driver.find_element(By.XPATH, "//button[@class= 'button-2 apply-shipping-button']").click()
        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.ID, "checkout").click()

