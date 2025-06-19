class DriverFactory:
    def __init__(self, browser_name):
        self.browser_name = browser_name

    def create_driver(self):
        if self.browser_name.lower() == "chrome":
            from selenium import webdriver
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # Run headless if needed
            return webdriver.Chrome(options=options)
        elif self.browser_name.lower() == "firefox":
            from selenium import webdriver
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")  # Run headless if needed
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")

    @staticmethod
    def quit_driver(driver):
        if driver:
            driver.quit()