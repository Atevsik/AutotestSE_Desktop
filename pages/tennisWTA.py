from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TennisWTA:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/tennis/wta/')

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH,"//div[contains(text(),'Статьи')]")

    def news(self):
        news = self.browser.find_element(By.XPATH,"//div[@class='se-newsline']//section[@class='se-titled-block']")

    def tournir(self):
        tournir = self.browser.find_element(By.XPATH,"//a[contains(text(),'Турниры')]")
        tournir.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/wta/', "Не правильный ВТА"

    def match(self):
        match = self.browser.find_element(By.XPATH,"//tbody/tr[10]/td[2]/a[1]")
        match.click()
        sleep(4)
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/wta/Singapore/2025/', "Не правильный матч"
        self.browser.back()

    def god(self):
        god = self.browser.find_element(By.XPATH,"//select[@class='common_height_26 mb_10']")
        god.click()
        select = Select(god)
        select.select_by_index(3)
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/wta/2022/', "Не правильный год"

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")










