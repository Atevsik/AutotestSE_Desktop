from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class ComandDiviz:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/L/khl/2023-2024/teams/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def deviz(self,count):
        deviz = self.browser.find_elements(By.XPATH,'//div[@class="sp-competition-teams__group-title"]')
        assert len(deviz) == count

    def knopki(self):
        knopki = self.browser.find_element(By.XPATH,"//div[@class='sp-competition-teams']//div[1]//div[2]//div[2]//div[5]//div[1]//div[2]//div[2]")

    def spartak(self):
        spartak = self.browser.find_element(By.XPATH, "//img[@title='Спартак']")
        spartak.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/spartak-hokkey-513/', "Не правильный урл спартака"
        self.browser.back()

    def filtri(self):
        filtri = self.browser.find_element(By.XPATH,"//div[@class='css-kxyrhr-control']")
        filtri.click()
