from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class McFootball:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/live/')

    def football_mc(self):
        football_mc = self.browser.find_element(By.XPATH, "(//a[@class='se-matchcenter-sports-list__row'])[1]")
        football_mc.click()

    def filtr_date(self):
        filtr_date = self.browser.find_element(By.XPATH,"//div[@data-component='matchcenter-filter']")

    def knopka_kalendar(self):
        knopka_kalendar = self.browser.find_element(By.XPATH, "//button[@class='react-date-picker__calendar-button react-date-picker__button']")

    def tomorow(self):
        tomorow = self.browser.find_element(By.XPATH,"//a[contains(text(),'Завтра')]")
        tomorow.click()

    def logo_bok(self):
        logo_bok = self.browser.find_element(By.XPATH,"//div[@class='se-matchcenter-sports-list__bookie']")

    def stavki(self):
        stavki = self.browser.find_element(By.XPATH,"//div[@class='se-matchcenter-match-extra__bets']")

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def navigator_sport(self):
        navigator_sport = self.browser.find_element(By.XPATH,"//div[@class='se-sport-navigator__sport']")
        navigator_sport.click()

    def regbi(self):
        regbi = self.browser.find_element(By.XPATH,"//div[@id='react-select-sports-option-0-12']//div[1]")
        regbi.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/live/rugby/', "Не правильный урл регби"

    def read_news(self):
        read_news = self.browser.find_element(By.XPATH,"//a[contains(text(),'Читать новости')]")
        read_news.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/rugby/news/'

