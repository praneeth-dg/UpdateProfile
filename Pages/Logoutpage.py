class LogoutPage():

    def __init__(self, driver):
        self.driver = driver

        self.logout_Parent_xpath = "//div[contains(text(),'My Naukri')]"
        self.logout_Child_xpath = "//a[@class='logout-gnb']]"

    def get_Parent(self):
        return self.driver.find_element_by_xpath(self.logout_Parent_xpath)


    def click_Child(self):
        self.driver.find_element_by_xpath(self.logout_Child_xpath).click()




