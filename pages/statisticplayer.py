from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class StatisticPlayer:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/player/56936/seasons/2023-2024/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def kard(self):
        kard = self.browser.find_element(By.XPATH,"//div[@class='se19-player-card']")

    def infkard(self):
        infkard = self.browser.find_element(By.XPATH,"//b[contains(text(),'Полузащитник')]")

    def match(self):
        match = self.browser.find_element(By.XPATH, "//td[normalize-space()='29.04.2024']")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def sopernik(self):
        sopernik = self.browser.find_element(By.XPATH,"//a[contains(text(),'Соперники')]")
        sopernik.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/56936/rivals/', "Соперники не правильный урл"

    def dinamo(self):
        dinamo = self.browser.find_element(By.XPATH,"//tbody/tr[14]/td[2]/a[1]")

    def legend(self):
        legend = self.browser.find_element(By.XPATH,"//td[contains(text(),'- красная карточка')]")
