#page locators
#page actions
#webdriver -Initialization
#custom Functions
#No assertions here(These are not test cases)
#page class


from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class Login_page():

    # webdriver initialization
    def __int__(self,driver):
        self.driver=driver

    # page locators

    username=(By.ID,"login-username")
    password=(By.NAME,"password")
    submit_button=(By.XPATH,"//button[@id='js-login-btn']")
    error_msg=(By.CSS_SELECTOR,"#js-notification-box-msg")

    # forgot pass, start a free trial,..... We skip as of now - u

    # Return a Webelements

    def get_username(self):
        return self.driver.find_element(*Login_page.username)

    def get_password(self):
        return self.driver.find_element(*Login_page.password)
    def get_submit(self):
        return self.driver.find_element(*Login_page.submit_button)
    def get_error_message(self):
        return self.driver.find_element(*Login_page.error_msg)

    #Page actions

    def login_to_awo(self,user,pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submit().click()
        # get username and send keys - email
        # get password and send keys - password
        # click the submit button and navigate to dashboard Page







