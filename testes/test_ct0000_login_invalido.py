import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.skip
class TestCT00000:
    def test_ct0000_login_inval(self):

        ##LOGIN
        pag0_login = LoginPage()
        pag0_login.fazer_login('testeraffaelial@gmail.com', 'Tesxxxxx@')

