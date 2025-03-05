from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class Trener:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/L/khl/2023-2024/trainers/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def nikitin(self):
        nikitin = self.browser.find_element(By.XPATH,"//img[@title='Никитин Игорь']")
        nikitin.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/trainer/101/', "Не правильный урл никита"
        self.browser.back()

    def knoka(self):
        knopka = self.browser.find_element(By.XPATH,"//div[@class='se-button']")
        knopka.click()

    def spisok(self,count):
        spisok = self.browser.find_elements(By.XPATH,"//td[@class='se-advanced-table-cell']")
        assert len(spisok) == count

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Тренеры')]")

    def table(self):
        table = self.browser.find_element(By.XPATH,"//div[@class='sp-tourtable']//div[@class='se-titled-block se-titled-block--bg-white']")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888'][1]")



