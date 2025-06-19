# tests/TestSelenium.py

import pytest
from src.utilities.driver_factory import DriverFactory

@pytest.fixture(scope="module")
def setup_driver():
    driver = DriverFactory.get_driver()
    yield driver
    DriverFactory.quit_driver(driver)

def test_home_page_title(setup_driver):
    driver = setup_driver
    driver.get("https://oc3032std.opencartlab.pl/")
    assert "Sklep demonstracyjny" in driver.title
