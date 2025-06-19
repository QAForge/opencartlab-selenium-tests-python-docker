class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://oc3032std.opencartlab.pl/"
    
    def navigate(self):
        self.driver.get(self.url)
    
    def is_title_correct(self):
        return "Sklep demonstracyjny" in self.driver.title