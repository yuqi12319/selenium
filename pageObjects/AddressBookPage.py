from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile

class AddressBookPage():
    def __init__(self,driver):
        self.driver = driver
        self.parseCf = ParseConfigFile()
        self.addContactsOptions =self.parseCf.getItemsSection("126mail_addContactsPage")

    def creatContactPersonButton(self):
        try:
            locatetype, locatorExpression = self.addContactsOptions["addContactsPage.createContactsBtn".lower()].split(">")
            elementObj = getElement(self.driver,locatetype,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonName(self):
        try:
            locatetype, locatorExpression = self.addContactsOptions["addContactsPage.contactPersonName".lower()].split(">")
            elementObj = getElement(self.driver, locatetype, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonEmail(self):
        try:
            locatetype, locatorExpression = self.addContactsOptions["addContactsPage.contactPersonEmail".lower()].split(">")
            elementObj = getElement(self.driver, locatetype, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def starContacts(self):
        try:
            locatetype, locatorExpression = self.addContactsOptions["addContactsPage.starContacts".lower()].split(">")
            elementObj = getElement(self.driver, locatetype, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonMobile(self):
        try:
            locatetype, locatorExpression = self.addContactsOptions["addContactsPage.contactPersonMobile".lower()].split(">")
            elementObj = getElement(self.driver, locatetype, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonComment(self):
        try:
            locatetype, locatorExpression = self.addContactsOptions["addContactsPage.contactPersonComment".lower()].split(">")
            elementObj = getElement(self.driver, locatetype, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def saveContacePerson(self):
        try:
            locatetype, locatorExpression = self.addContactsOptions["addContactsPage.savecontacePerson".lower()].split(">")
            elementObj = getElement(self.driver, locatetype, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    