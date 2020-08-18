from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile

class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.loginOption = self.parseCF.getItemsSection("126mail_login")

    def clickLbNormal(self):
        try:
            locatetype, locatorExpression = self.loginOption["loginPage.clickLbNormal".lower()].split(">")
            elementObj = getElement(self.driver,locatetype,locatorExpression)
            return elementObj
        except Exception as e:
            raise e


    def switchToFrame(self):
        try:
            locatetype, locatorExpression = self.loginOption["loginPage.frame".lower()].split(">")
            elementObj = getElement(self.driver,locatetype,locatorExpression)
            self.driver.switch_to.frame(elementObj.get_attribute("id"))
        except Exception as e:
            raise e

    def swithToDefaultFrame(self):
        self.driver.switch_to.default_content()

    def userNameObj(self):
        try:
            locatetype,locatorExpression = self.loginOption["loginPage.username".lower()].split(">")
            elementObj = getElement(self.driver,locatetype,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def passwoedObj(self):
        try:
            locatetype,locatorExpression = self.loginOption["loginPage.password".lower()].split(">")
            elementObj = getElement(self.driver,locatetype,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def loginButton(self):
        try:
            locatetype,locatorExpression = self.loginOption["loginPage.loginbutton".lower()].split(">")
            elementObj = getElement(self.driver,locatetype,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox(executable_path="G:\pycharm\python_workspace\webdriver\geckodriver.exe")
    driver.get("http://mail.126.com")
    import time
    time.sleep(2)
    login = LoginPage(driver)
    login.clickLbNormal().click()
    login.switchToFrame()
    # driver.find_element_by_id("lbNormal").click()
    # driver.switch_to.frame(driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe').get_attribute("id"))
    login.userNameObj().send_keys("xxx")
    login.passwoedObj().send_keys("xxx")
    login.loginButton().click()
    login.swithToDefaultFrame()
    driver.quit()