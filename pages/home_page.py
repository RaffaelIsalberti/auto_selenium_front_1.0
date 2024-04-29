import conftest
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        self.driver = conftest.driver
        self.valid_home = (By.XPATH, "// h2[text() = 'Welcome to our store']")
        self.actions = ActionChains(self.driver)

        #selecionar sessao de computadores
        self.opc_shop = (By.XPATH, "//a[text() ='Computers ']")
        self.prod_sh = (By.XPATH, "//a[text() ='Notebooks ']")

        #adicionar primeiro produto sessão de computadores
        self.check_opc = (By.ID, 'attribute-option-7')
        #self.prod_sh1 = (By.XPATH, "//*[contains(text(), 'Asus N551JK-XO076H Laptop')]")
        #self.prod_sh1 = (By.XPATH, "//h2[@class='product-title']/a[text()='Asus N551JK-XO076H Laptop']")
        self.prod_sh1 = (By.CSS_SELECTOR, "h2.product-title > a[href$='asus-n551jk-xo076h-laptop']")

        #SELECIONAR CAMPO QUANTIDADE
        self.check_qtd = (By.ID, "product_enteredQuantity_5")

        #adicionar segundo produto sessão de eletronicos
        self.opc_shop1 = (By.XPATH, "//ul[1]/li[2]/a[text()='Electronics ']")
        self.prod_sh2 = (By.XPATH, "//div[2]/ul[1]/li[2]/ul/li[2]/a[text()='Cell phones ']")
        self.prod_shop2 = (By.XPATH, "//h2/a[text()='Nokia Lumia 1020']")

    def valid_home_pag(self):
        self.disp_valid(self.valid_home)

#NAVEGAÇÃO LOJA COMPUTADOR
    def move_to_sessao(self):
        self.move_to_element(self.opc_shop)

    def sel_opc_prod(self):
        self.move_to_element(self.prod_sh)
        self.cliq(self.prod_sh)

#COMPRA PRIMEIRO PRODUTO
    def buy_product(self):
        self.marca_opc()
        self.add_ao_cart()
       # self.wait_add_to_cart()

    def marca_opc(self):
        self.cliq(self.check_opc)
        pass

    def add_ao_cart(self):
        self.cliq(self.prod_sh1)
    pass

    def wait_add_to_cart(self):
        self.wait_to_element(self.add_ao_cart)


#LIMPAR CAMPO QTD

    def find_field_qtd(self):
        self.db_to_click()
        self.del_qtd()
        self.inf_qtd('2')

    def db_to_click(self):
        self.double_cliq(self.check_qtd)
        pass

    def del_qtd(self): ##ajustar função para deletar
        self.button_del(self.check_qtd)
        pass

    def inf_qtd(self, qtd):
        self.writer(self.check_qtd, qtd)
        pass

#NAVEGAÇÃO LOJA ELETRONICOS
    def shop_eletrc(self):
        self.mover_ao_cart()
        self.mover_ao_prod()
        self.add_prod_ao_cart2('Nokia Lumia 1020')

    def mover_ao_cart(self):
        self.move_to_element(self.opc_shop1)
        pass

    def mover_ao_prod(self):
        self.move_to_element(self.prod_sh2)
        pass

    def add_prod_ao_cart2(self, nome_prod2):
        self.cliq(self.prod_sh2)
        product = (self.prod_shop2[0], self.prod_shop2[1].format(nome_prod2))
        self.cliq(product)
        pass
