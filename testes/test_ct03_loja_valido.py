import pytest
import conftest
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

        ##FUNÇÃO MOUSE HOVER - MOUSE FLUTUANTE
        home_page.move_to_sessao()
        home_page.sel_opc_prod()

        ##NAVEGAÇÃO LOJA NOTEBOOK
        home_page.buy_product()

        ##FUNÇÃO DOUBLE CLICK MOUSE e SCROLL #limpar campo de quantidade para preenchimento
        home_page.find_field_qtd()

        ##ADICIONAR ITEM
        driver.find_element(By.ID, "add-to-cart-button-5").click()

        ##FECHAR MENSAGEM
        assert driver.find_element(By.XPATH, "//p[text()= 'The product has been added to your ']").is_displayed()
        driver.find_element(By.XPATH, "//span[@class='close']").click()

        ##MOUSE HOPER CARRINHO
        home_page.aces_cart()

        ##MOUSE HOPER LOJA ELETRONICOS
        home_page.shop_eletrc()

        ##FECHAR MENSAGEM
        assert driver.find_element(By.XPATH, "//p[text()= 'The product has been added to your ']").is_displayed()
        driver.find_element(By.XPATH, "//span[@class='close']").click()

        ##acessar cart 2
        home_page.aces_cart()

        #ESTIMAR ENVIO
        home_page.calc_fret()

        #FECHAR COMPRA
        home_page.checkout_shop()


