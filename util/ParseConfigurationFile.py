#用于解析存储定位页面元素的定位表达式文件，以便获取定位表达式

from config.VarConfig import pageElementLocatorPath
from configparser import ConfigParser

class ParseConfigFile():
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemsSection(self, sectionName):
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self, sectionName, optionName):
        value = self.cf.get(sectionName,optionName)
        return value

if __name__ == '__main__':
    pc = ParseConfigFile()
    print(pc.getItemsSection("126mail_login"))
    print(pc.getOptionValue("126mail_login","loginPage.clickLbNormal"))