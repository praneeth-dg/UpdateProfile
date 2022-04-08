import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Pages.Loginpage import LoginPage
from Pages.UpdatePage import UpdateProfile
from Pages.Logoutpage import LogoutPage
from Utils import Utils as Utils


@pytest.mark.usefixtures("test_setup")
class TestUpdate():

    def test_LoginPage(self):
        driver = self.driver
        driver.get(Utils.URL)
        time.sleep(2)
        login = LoginPage(driver)
        time.sleep(3)
        login.enter_username(Utils.username)
        login.enter_password(Utils.Password)
        login.click_submit()
        print("Page login succesfully")

    def test_UpdateProfile(self):
        time.sleep(2)
        driver = self.driver
        Update = UpdateProfile(driver)
        time.sleep(3)
        Update.click_languages()
        time.sleep(5)
        Update.click_female()
        Update.click_male()
        Update.click_Save()
        print("Profile Updated")

    def test_LogoutPage(self):
        time.sleep(3)
        driver = self.driver
        #Currtime = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        #ScreenshotName = "screenshot_"+Currtime
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotName",
                      attachment_type=allure.attachment_type.PNG)
        logout = LogoutPage(driver)
        action = ActionChains(driver)
        parent_level_menu = driver.find_element_by_xpath("//div[contains(text(),'My Naukri')]")
        action.move_to_element(parent_level_menu).perform()
        child_level_menu = driver.find_element_by_xpath("//a[@class='logout-gnb']")
        child_level_menu.click();