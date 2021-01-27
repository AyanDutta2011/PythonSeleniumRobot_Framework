import unittest
from selenium import webdriver

class DemoSite(unittest.TestCase):

    @classmethod
    def test_setupClass(self):     # Execute once before class started
        self.driver = webdriver.Chrome()
        self.driver.get("http://demo.automationtesting.in/Register.html")

    @classmethod
    def test_tearDownClass(self):    # Execute once before class ended
        self.driver.close()

    @classmethod
    def test_setUp(cls):   # Execute once before methods started
        print("Test Case is execution is in progress")

    @classmethod
    def test_tearDown(cls):  # Execute once before method ended
        print("Test Case execution is completed")

    def test_TC1(self):
        print("Title of the webpage is " + self.driver.title)

    def test_TC2(self):
        print("Title of the webpage is " + self.driver.title)

if __name__ == "__main__":
    unittest.main()

