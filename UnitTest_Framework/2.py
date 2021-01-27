import unittest
from selenium import webdriver

class DemoSite(unittest.TestCase):

    def test_TC1(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://demo.automationtesting.in/Register.html")
        print("Title of the webpage is " + self.driver.title)
        self.driver.close()

    @unittest.SkipTest    #Skipping test
    def test_TC2(self):
        print("feature1")

    @unittest.SkipTest("Incomplete")   #Skipping test with message
    def test_TC3(self):
        print("feature2")

    @unittest.SkipTest(1==1,"Numbers are not equal")  #Skipping test when condition satisfy
    def test_TC4(self):
        print("feature3")

    def test_TC5(self):
        print("feature4")

    def test_TC6(self):
        print("feature5")

if __name__ == "__main__":
    unittest.main()