class UpdateProfile():

    def __init__(self, driver):
        self.driver = driver
        self.Link_Languages_xpath = "//a[contains(text(),'Add Languages')]"
        self.Radiobutton_Female_xpath = "//label[contains(text(),'Female')]"
        self.Radiobutton_Male_xpath = "//label[contains(text(),'Male')]"
        self.button_Save_id = "//button[@id='savePersonalDetailsBtn']"


    def click_languages(self):
        self.driver.find_element_by_xpath(self.Link_Languages_xpath).click()

    def click_female(self):
        self.driver.find_element_by_xpath(self.Radiobutton_Female_xpath).click()

    def click_male(self):
        self.driver.find_element_by_xpath(self.Radiobutton_Male_xpath).click()

    def click_Save(self):
        self.driver.find_element_by_xpath(self.button_Save_id).click()


