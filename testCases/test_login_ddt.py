import inspect
import time
from pageObjects.LoginPage import LoginPage
from testCases.configTest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_Login_002_DDT:
    basePath = ReadConfig.basePath()
    baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUserEmai()
    # password = ReadConfig.getPassword()
    path = basePath+"/TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("######## Test case2 DDT started ########")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows: ", self.rows)

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPasswod(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                assert True
                self.logger.info("######## Test case passed ########")
                self.driver.close()
            else:
                self.driver.save_screenshot(self.basePath+"/Screenshots/"+type(self).__name__+"[ "+inspect.stack()[0][3]+" ].png")
                self.logger.error("######## Test case failed ########")
                self.driver.close()
                assert False


