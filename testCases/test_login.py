import inspect

import pytest

from pageObjects.LoginPage import LoginPage
from testCases.configTest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login_001:
    basePath = ReadConfig.basePath()
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmai()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homepageTitle(self, setup):
        self.logger.info("######## Test case1 started ########")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("######## Test case passed ########")
            self.driver.close()
        else:
            self.driver.save_screenshot(self.basePath+"/Screenshots/"+type  (self).__name__+"[ "+inspect.stack()[0][3]+" ].png")
            self.driver.close()
            self.logger.info("######## Test case failed ########")
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("######## Test case2 started ########")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPasswod(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("######## Test case passed ########")
            self.driver.close()
        else:
            self.driver.save_screenshot(self.basePath+"/Screenshots/"+type(self).__name__+"[ "+inspect.stack()[0][3]+" ].png")
            self.logger.info("######## Test case failed ########")
            self.driver.close()
            assert False


