from selenium import webdriver
from appModules.LoginAction import LoginAction
import time

def testMailLogin():
    try:
        driver = webdriver.Firefox(executable_path="G:\pycharm\python_workspace\webdriver\geckodriver.exe")
        driver.get("http://mail.126.com")
        driver.implicitly_wait(30)
        driver.maximize_window()
        LoginAction.login(driver,username="xxx",password="xxx")
        assert u"未读邮件" in driver.page_source
    except Exception as e:
        raise e
    finally:
        driver.quit()

if __name__ == '__main__':
    testMailLogin()
    print(u"登陆126邮箱成功")