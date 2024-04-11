import pytest
from selenium import webdriver
driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    #setup
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")

    #run test
    yield

    #teardown
    driver.quit()
