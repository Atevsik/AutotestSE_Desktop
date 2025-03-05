from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalendarGame:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2024-2025/calendar/tours/')

    def main_book(self):
        main_book = self.browser.find_element(By.XPATH,"//div[@class='se19-main-content__extra']")

    def match(self):
        match = self.browser.find_element(By.XPATH, "//tbody/tr[6]/td[3]/div[1]/p[1]/a[1]")
        match.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/rfpl/fbl_match-orenburg-spartak-397433/', "Не правильный урл матча"
        self.browser.back()

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH, "//div[@id='adfox_15645683733586888']")










