from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Mc1:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/live/')
        sleep(6)

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH, "//div[@id='adfox_15645683733586888']")

    def booker(self):
        booker = self.browser.find_element(By.XPATH, "//div[@class='se-matchcenter-sports-list__bookie']")

    def vid_materiala(self):
        vid_materiala = self.browser.find_element(By.XPATH,"//div[@class='swiper-wrapper']")

    def filtr_date(self):
        filtr_date = self.browser.find_element(By.XPATH,"//div[@data-component='matchcenter-filter']")

    def football_mc(self):
        football_mc = self.browser.find_element(By.XPATH, "(//a[@class='se-matchcenter-sports-list__row'])[1]")
        football_mc.click()

    def logo_bok(self):
        logo_bok = self.browser.find_element(By.XPATH,"//div[@class='se-matchcenter-sports-list__bookie']")

    def stavki(self):
        stavki = self.browser.find_element(By.XPATH,"//div[@class='se-matchcenter-match-extra__bets']")

