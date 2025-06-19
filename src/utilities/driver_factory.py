# src/utilities/driver_factory.py

from selenium import webdriver

class DriverFactory:
    def __init__(self, browser_name):
        self.browser_name = browser_name

    def create_driver(self):
        if self.browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            return webdriver.Chrome(options=options)
        elif self.browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")

    @staticmethod
    def quit_driver(driver):
        if driver:
            driver.quit()

    @staticmethod
    def get_driver():
        factory = DriverFactory("chrome")
        return factory.create_driver()
