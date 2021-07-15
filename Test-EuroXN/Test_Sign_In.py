import sys
import unittest
import random
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from time import sleep

login = "dmitriy.r+67@pandats.com"
password = "123456789A"



class MainPageTest(unittest.TestCase):

    def setUp(self):
        dr = "C:\python\drivers\chromedriver.exe"
        self.driver = webdriver.Chrome(dr)

    def test_Sign_In(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.euroxn.com/trade-room/?#/")
        driver.implicitly_wait(15)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[1]").click()
        sleep(5)
        EN = driver.find_element_by_xpath("//div[contains(text(),'Volume in lot')]").text
        assert "Volume in lot" in EN
        print("ENGLISH: " + EN)



        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[2]").click()
        sleep(5)
        DE = driver.find_element_by_xpath("//div[contains(text(),'Volumen in Lot')]").text
        assert "Volumen in Lot"  in DE
        print("GERMANY: " + DE)


        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[3]").click()
        sleep(5)
        RU = driver.find_element_by_xpath("//div[contains(text(),'Объем в лотах')]").text
        assert "Объем в лотах" in RU
        print("RUSSIAN " + RU)


        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[4]").click()
        sleep(5)
        KR = driver.find_element_by_xpath("//div[contains(text(),'로트 볼륨')]").text
        assert "로트 볼륨"in KR
        print("KOREAN: " + KR)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[5]").click()
        sleep(5)
        AR = driver.find_element_by_xpath("//div[contains(text(),'الحجم بالحصة')]").text
        assert  "الحجم بالحصة" in AR
        print("ARABIC: " + AR)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[6]").click()
        sleep(5)
        ES = driver.find_element_by_xpath("//div[contains(text(),'Volumen en lote')]").text
        assert "Volumen en lote" in ES
        print("ESPANOL: " + ES)


        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[7]").click()
        sleep(5)
        FR = driver.find_element_by_xpath("//div[contains(text(),'Volume par lot')]").text
        assert "Volume par lot" in FR
        print("FRANCH : " + FR)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[8]").click()
        sleep(5)
        GE = driver.find_element_by_xpath("//div[contains(text(),'პარტიის მოცულობა')]").text
        assert "პარტიის მოცულობა" in GE
        print("GEORGIE: " + GE)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[9]").click()
        sleep(5)
        HU = driver.find_element_by_xpath("//div[contains(text(),'Lotban megadott volumen')]").text
        assert "Lotban megadott volumen" in HU
        print("HUNGARY: " + HU)


        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[10]").click()
        sleep(5)
        IT = driver.find_element_by_xpath("//div[contains(text(),'Volume in lotto')]").text
        assert "Volume in lotto" in IT
        print("ITALY: " + IT)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[11]").click()
        sleep(5)
        PL = driver.find_element_by_xpath("//div[contains(text(),'Ilość w locie')]").text
        assert "Ilość w locie" in PL
        print("POLSKI: " + PL)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[12]").click()
        sleep(5)
        PT = driver.find_element_by_xpath("//div[contains(text(),'Volume em lote')]").text
        assert "Volume em lote" in PT
        print("PORTUGAL: " + PT)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[13]").click()
        sleep(5)
        RO = driver.find_element_by_xpath("//div[contains(text(),'Volum în lot')]").text
        assert "Volum în lot" in RO
        print("ROMANE: " + RO)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[14]").click()
        sleep(5)
        TR = driver.find_element_by_xpath("//div[contains(text(),'Lot Hacmi')]").text
        assert "Lot Hacmi" in TR
        print("TURKEY: " + TR)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[15]").click()
        sleep(5)
        TH = driver.find_element_by_xpath("//div[contains(text(),'ปริมาณในล็อต')]").text
        assert "ปริมาณในล็อต" in TH
        print("THAILAND: " + TH)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[16]").click()
        sleep(5)
        CH = driver.find_element_by_xpath("//div[contains(text(),'交易量（手）')]").text
        assert "交易量（手）" in CH
        print("CHINA: " + CH)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[17]").click()
        sleep(5)
        CZ = driver.find_element_by_xpath("//div[contains(text(),'Objem v lotech')]").text
        assert "Objem v lotech" in CZ
        print("CZECH: " + CZ)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[18]").click()
        sleep(5)
        NL = driver.find_element_by_xpath("//div[contains(text(),'Volume in partij')]").text
        assert "Volume in partij" in NL
        print("NEDERLANDS: " + NL)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[19]").click()
        sleep(5)
        ID = driver.find_element_by_xpath("//div[contains(text(),'Volume in lot')]").text
        assert "Volume in lot" in ID
        print("INDIA: " + ID)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[20]").click()
        sleep(5)
        ML = driver.find_element_by_xpath("//div[contains(text(),'Jumlah dalam lot')]").text
        assert "Jumlah dalam lot" in ML
        print("MELAYU: " + ML)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[21]").click()
        sleep(5)
        JP = driver.find_element_by_xpath("//div[contains(text(),'ロット量')]").text
        assert "ロット量" in JP
        print("JAPAN: " + JP)

        driver.find_element_by_id("hamburger_icon").click()
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Choose trading platform language')]").click()
        sleep(2)
        driver.find_element_by_xpath("//ul[@id = 'lang-dropdown']/li[22]").click()
        sleep(5)
        VI = driver.find_element_by_xpath("//div[contains(text(),'Volume in lot')]").text
        assert "Volume in lot" in VI
        print("VIETNAM: " + VI)



if __name__ == "__main__":
    unittest.main()