import time

import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
#@pytest.mark.skip
class TestCT0002:
    def test_ct0002_login_val(self):
        driver = conftest.driver

        ##LOGIN teste login
        pag_login = LoginPage()
        time.sleep(2)
        pag_login.fazer_login("testeraffaelial@gmail.com", "Teste123@")
        time.sleep(2)
        assert driver.find_element(By.XPATH, "// h2[text() = 'Welcome to our store']")
