from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class CardPlayer:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/player/2283/seasons/2023-2024/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def info(self):
        info = self.browser.find_element(By.XPATH, "//table[@class='se19-table-player-card']")

    def match(self):
        match = self.browser.find_element(By.XPATH,"//td[normalize-space()='26.03.2024']")

    def click_match(self):
        click_match = self.browser.find_element(By.XPATH,"//a[normalize-space()='0 : 3']")
        click_match.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/euro/fbl_match-turciya-portugaliya-388571/', "Не правильный матч"
        self.browser.back()

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def filtr(self):
        filtr = self.browser.find_element(By.XPATH,"//div[@class='cusel_select mr_20']")
        filtr.click()

