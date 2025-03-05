from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class MmaRaiting:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/fighting/mma/ufc/2024/ratings/men/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def boets(self,count):
        boets = self.browser.find_elements(By.XPATH,"//div[@class='sp-ratings__fighter-info']")
        assert len(boets) == count

    def champion(self):
        champion = self.browser.find_element(By.XPATH,"//div[@class='se-fighter-champion-panel se-fighter-champion-panel--champion-mma']")

    def stolb(self,count):
        stolb = self.browser.find_elements(By.XPATH,"//th[@class='se-advanced-table-cell']")
        assert len(stolb) == count

    def japan(self):
        japan = self.browser.find_element(By.XPATH,"//a[contains(text(),'Тацуро Тайра')]")
        japan.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/tacuro-tayra-26076/', "Не правильный урл бойца"
        self.browser.back()

    def prom(self):
        prom = self.browser.find_element(By.XPATH,"//div[@class='se-sport-navigator__competition']")
        prom.click()

    def prom1(self):
        prom1 = self.browser.find_element(By.XPATH,"//div[@id='react-select-competitions-option-0-4']")
        prom1.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/fighting/mma/aca/2025/calendar/', "Не правильный урл АСА"

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def seson(self):
        seson = self.browser.find_element(By.XPATH,"//div[@class='se-sport-navigator__season']")
        seson.click()

    def seson2(self):
        seson2 = self.browser.find_element(By.XPATH,"//div[@id='react-select-seasons-option-0-1']")
        seson2.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/fighting/mma/aca/2024/calendar/', "Не правильный год"

    def raitingi(self):
        raitingi = self.browser.find_element(By.XPATH,"//div[@class='se-page-menu-item']//a[contains(text(),'Рейтинги')]")
        raitingi.click()

    def dopprover(self):
        dopprover = self.browser.find_element(By.XPATH,"//a[contains(text(),'Юнус Евлоев')]")
