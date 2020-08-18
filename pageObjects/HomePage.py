from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile

class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()

    def addressLink(self):
        try:
            locatetype, locatorExpression = self.parseCF.getOptionValue("126mail_homePage","homePage.addressbook").split(">")
            elementObj = getElement(self.driver,locatetype,locatorExpression)
            return elementObj
        except Exception as e:
            raise e