import unittest
from selenium import webdriver

class DemoSite(unittest.TestCase):

    def test_TC1(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://demo.automationtesting.in/Register.html")
        web_title = self.driver.title
        print("Title of the webpage is " + web_title)

        self.assertEqual("Register", web_title, "Title is not matched")
        self.assertNotEqual("Ayan", web_title, "Title Matched")
        self.assertTrue(web_title == "Register")
        self.assertFalse(web_title == "Ayan")
        empty = None
        self.assertIsNone(empty)
        self.assertIsNotNone(web_title)
        self.driver.close()

    def test_TC2(self):
        list = {"Ayan", "Aparna", "Chandra"}
        self.assertIn("Aparna", list)
        self.assertNotIn("Neha", list)
        print("Complete1")

    def test_TC3(self):
        self.assertGreater(200,100)
        self.assertGreaterEqual(20,20)
        self.assertNotEqual(99,69)
        self.assertLess(10,100)
        self.assertLessEqual(10,10)
        print("Complete2")

if __name__ == "__main__":
    unittest.main()