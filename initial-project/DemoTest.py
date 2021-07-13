import unittest
import random
from selenium.webdriver.support.ui import Select
from selenium import webdriver



def random_name():
    str1 = "qwertpasdfgfhghllzcbnbvmn"
    ls = list(str1)
    random.shuffle(ls)
    psw = ''.join([random.choice(ls) for x in range(6)])
    ex3 = (psw)
    return ex3


def random_email():
    str1 = "qwertpasdfgfhghllzcbnbvmn"
    str2 = "1234567890"
    prefix = "@pandats.com"
    ls = list(str1 + str2)
    random.shuffle(ls)
    psw = ''.join([random.choice(ls) for x in range(6)])
    ex3 = (psw + prefix)
    return ex3

def random_phone():
    str1 = '1234567890'
    ls = list(str1)
    random.shuffle(ls)
    psw = ''.join([random.choice(ls) for x in range(10)])
    ex3 = psw
    return ex3

def random_password():
    str1 = "qwertpasdfgfhghllzcbnbvmn"
    str2 = "1234567890"
    ls = list (str1+str2)
    psw = ''.join([random.choice(ls) for x in range(8)])
    ex4 = psw + "Aa"
    return ex4


class DemoTestPage(unittest.TestCase):
    def setUp(self):
        dr = "C:\python\drivers\chromedriver.exe"
        self.driver = webdriver.Chrome(dr)

    def test_SignUp(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.euroxn.com/#/")
        driver.implicitly_wait(5)

#FirstName
        driver.find_element_by_id("firstName").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys(random_name())

#LastName
        driver.find_element_by_id("lastName").click()
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys(random_name())

#Email
        driver.find_element_by_xpath("//div[@class = 'col s12 m12 l12']/input[@id = 'email']").click()
        driver.find_element_by_xpath("//div[@class = 'col s12 m12 l12']/input[@id = 'email']").clear()
        driver.find_element_by_xpath("//div[@class = 'col s12 m12 l12']/input[@id = 'email']").send_keys(random_email())

#Country
        select = Select(driver.find_element_by_id("country"))
        select.select_by_value("AL")

#Phone
        driver.find_element_by_id("phone").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys(random_phone())

#Password
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        double_pss = driver.find_element_by_id("password").send_keys(random_password())

#Confirm_Password
        driver.find_element_by_id("confirm_password").click()
        driver.find_element_by_id("confirm_password").clear()
        driver.find_element_by_id().send_keys(double_pss)

#Checkbox_Terms
        driver.find_element_by_id("//input[@id = 'terms']").click()
        driver.get_screenshot_as_file("screen2.png")






if __name__ == "__main__":
    unittest.main()
