import time
import pytest
from selenium import webdriver


#lets import our requirements from page objects module
from tests2.pageObjects.LoginPage import Login_page


class TestVWOLogin():

    @pytest.fixture()
    def driver(self):
        driver=webdriver.Chrome()
        driver.get("https://app.vwo.com")
        driver.maximize_window()
        yield driver
        driver.quit()

    @pytest.mark.positive
    def test_Vwo_Login(self,driver):
        loginpage=Login_page(driver)
        loginpage.login_to_awo("contact+augg@thetestingacademy.com", "Wingify@123")
        time.sleep(5)
        assert "Dashboard" in driver.title

        time.sleep(3)



