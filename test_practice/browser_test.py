from selenium import webdriver
import unittest
import warnings

class VisitBaidu(unittest.TestCase):
    #启动IE浏览器
    def setUp(self):
        warnings.simplefilter("ignore",ResourceWarning)
        self.driver = webdriver.Ie(executable_path="G:\pycharm\python_workspace\webdriver\IEDriverServer.exe")
        # self.driver = webdriver.Firefox(executable_path="G:\pycharm\python_workspace\webdriver\geckodriver.exe")
        # self.driver = webdriver.Chrome(executable_path="G:\pycharm\python_workspace\webdriver\chromedriver.exe")

    def test_visitBaidu(self):
        self.driver.get("http://www.baidu.com")
        # print(self.driver.current_url)

    #退出ie浏览器
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
