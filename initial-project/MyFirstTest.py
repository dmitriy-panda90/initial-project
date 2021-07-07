import time
import unittest
from selenium import webdriver


class TestPro(unittest.TestCase):

    def setUp(self):
        dr = "C:\python\drivers\chromedriver.exe"
        self.driver = webdriver.Chrome(dr)

    def test_search(self):
        driver = self.driver

        driver.get("https://github.com/")
        driver.fullscreen_window()

        # Sign in

        driver.find_element_by_link_text("Sign up").click()
        driver.fullscreen_window()

        timeWait = time.sleep(10)
        title = driver.title
        print(title)

        assert "GitHub · GitHub" in title

        email_p = "dmitriy.r+525@pandats.com"
        password = "123456789A"

        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(email_p)
        timeWait
        driver.find_element_by_xpath("//div[@id='email-container']//button[1]").submit()
        timeWait
        assert "Email is invalid or already taken" not in driver.page_source
        timeWait
        driver.get_screenshot_as_file("screenshot.png")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_xpath("//div[@id='email-container']//button[1]").submit()

        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)

   # def tearDown(self):
    #    self.driver.close()

if __name__ == "__main__":
        unittest.main()
