import unittest
import random

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def random_Name():
    str1 = "qwertpasdfgfhghllzcbnbvmn"
    ls = list(str1)
    random.shuffle(ls)
    psw = ''.join([random.choice(ls) for x in range(6)])
    ex3 = (psw)
    return ex3


class DemoTestPage2(unittest.TestCase):


  def setUp(self):
    dr = "C:\python\drivers\chromedriver.exe"
    self.driver = webdriver.Chrome(dr)


  def test_SignUp(self):
    driver = self.driver
    driver.get("https://www.euroxn.com/#/")
    driver.maximize_window()

    driver.find_element_by_id("firstName").click()
    driver.find_element_by_id("firstName").clear()
    driver.find_element_by_id("firstName").send_keys(random_Name())


if __name__ == "__main__":
    unittest.main()
