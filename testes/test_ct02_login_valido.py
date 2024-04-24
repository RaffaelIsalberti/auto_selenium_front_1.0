import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.skip
class TestCT0002:
    def test_ct0002_login_val(self):
        pag_login = LoginPage()
        pag_home = HomePage()

        ##LOGIN
        pag_login.fazer_login("testeraffaelial@gmail.com", "Teste123@")

        #VALIDAR LOGIN
        pag_home.valid_home_pag()