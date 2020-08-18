from pageObjects.LoginPage import LoginPage

class LoginAction():
    def __init__(self):
        print("login...")

    @staticmethod
    def login(driver,username,password):
        try:
            login = LoginPage(driver)
            login.clickLbNormal().click()
            login.switchToFrame()
            login.userNameObj().send_keys(username)
            login.passwoedObj().send_keys(password)
            login.loginButton().click()
            login.swithToDefaultFrame()
        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox(executable_path="G:\pycharm\python_workspace\webdriver\geckodriver.exe")
    driver.get("http://mail.126.com")
    LoginAction.login(driver,username="xxx",password="xxx")
    driver.quit()