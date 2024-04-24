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
        self.prod_sh1 = (By.XPATH, "//*[contains(text(), 'Asus N551JK-XO076H Laptop')]")

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
    def marca_opc(self):
        self.cliq(self.check_opc)

    def add_ao_cart(self):
        self.cliq(self.prod_sh1)
        pass

    def wait_add(self):
        self.wait_to_element(self.add_ao_cart())

#NAVEGAÇÃO LOJA ELETRONICOS
    def mover_ao_cart(self):
        self.move_to_element(self.opc_shop1)

    def mover_ao_prod(self):
        self.move_to_element(self.prod_sh2)

    def add_ao_cart2(self, nome_prod2):
        self.cliq(self.prod_sh2)
        product = (self.prod_shop2[0], self.prod_shop2[1].format(nome_prod2))
        self.cliq(product)
