import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
#@pytest.mark.skip
class TestCT0002:
    def test_ct0002_login_val(self):
        driver = conftest.driver
        pag_login = LoginPage()

        ##LOGIN
        pag_login.fazer_login("testeraffaelial@gmail.com", "Teste123@")

        #VALIDAR LOGIN
        assert driver.find_element(By.XPATH, "// h2[text() = 'Welcome to our store']").is_displayed()
