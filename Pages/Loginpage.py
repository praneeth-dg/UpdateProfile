class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "usernameField"
        self.password_textbox_id = "passwordField"
        self.Login_button_xpath = "//button[@data-ga-track='spa-event|login|login|Save']"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, Password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(Password)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.Login_button_xpath).click()
