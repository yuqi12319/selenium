import time
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
import traceback

class AddContactPerson():
    def __init__(self):
        print("add contact person")

    @staticmethod
    def add(driver,contactName,contactEmail,isStar,contactPhone,contactComment):
        try:
            hp = HomePage(driver)
            hp.addressLink().click()
            time.sleep(3)
            apb = AddressBookPage(driver)
            apb.creatContactPersonButton().click()
            if contactName:
                apb.contactPersonName().send_keys(contactName)
                apb.contactPersonEmail().send_keys(contactEmail)
            if isStar == u"是":
                apb.starContacts().click()
            if contactPhone:
                apb.contactPersonMobile().send_keys(contactPhone)
            if contactComment:
                apb.contactPersonComment().send_keys(contactComment)
            apb.saveContacePerson().click()
        except Exception as e:
            print(traceback.print_exc())
            raise e

if __name__ == '__main__':
    from appModules.LoginAction import LoginAction
    from selenium import webdriver
    import time
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(executable_path="G:\pycharm\python_workspace\webdriver\chromedriver.exe",chrome_options=chrome_options)
    driver.get("http://mail.126.com")
    # LoginAction.login(driver,"xxx","yyy")
    # AddContactPerson.add(driver,u"张三","zs@qq.com",u"是","","")
    # time.sleep(3)
    # assert u"张三" in driver.page_source
    driver.quit()