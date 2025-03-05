from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FigurkaNew:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/winter/figure-skating/grand-pri/2022-2023/calendar/')

    def filtrs(self):
        filtrs = self.browser.find_element(By.XPATH,"//div[@class='se-page-filters']")

    def itap(self):
        itap = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container']")
        itap.click()

    def america(self):
        america = self.browser.find_element(By.XPATH,"//div[contains(text(),'Skate America')]")
        america.click()

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='se-competition-titled-block__title']")

    def sports(self):
        sports = self.browser.find_element(By.XPATH,"//div[@class='se-page-menu-item']//a[contains(text(),'Спортсмены')]")
        sports.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/winter/figure-skating/grand-pri/2022-2023/players/', "Не правильный спортсмен"

    def text(self):
        text = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def dr(self):
        dr = self.browser.find_element(By.XPATH,"//div[contains(text(),'ДР')]")

    def rost(self):
        rost = self.browser.find_element(By.XPATH,"//div[contains(text(),'Рост')]")

    def flag(self,count):
        flag = self.browser.find_elements(By.XPATH,"//div[@class='se-file-image se-file-image--circle sp-competition-players-list__country-flag']")
        assert len(flag) == count

    def select(self):
        select = self.browser.find_element(By.XPATH,"//div[@class='se-select__value']")
        select.click()

    def germany(self):
        germany = self.browser.find_element(By.XPATH,"//div[@class='se-select__item'][contains(text(),'Германия')]")
        germany.click()

    def kol_vo(self,count):
        kol_vo = self.browser.find_elements(By.XPATH,"//td[@class='se-advanced-table-cell se-advanced-table-cell--sorted']")
        assert len(kol_vo) == count














