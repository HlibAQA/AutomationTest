import pytest
from selenium import webdriver


# function is default for fixture
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
