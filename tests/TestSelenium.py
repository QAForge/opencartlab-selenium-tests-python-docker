from selenium import webdriver
from src.utilities.driver_factory import DriverFactory
import pytest

@pytest.fixture(scope="module")
def setup_driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

def test_home_page_title(setup_driver):
    driver = setup_driver
    driver.get("https://oc3032std.opencartlab.pl/")
    assert "Sklep demonstracyjny" in driver.title