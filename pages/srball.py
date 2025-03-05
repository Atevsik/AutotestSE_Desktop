from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class SrBall:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2023-2024/statistics/estimation/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def triigroka(self,count):
        triigroka = self.browser.find_elements(By.XPATH,"//div[@class='se19-players-statistics__player se19-player-statistics']")
        assert len(triigroka) == count

    def perexod_igrok(self):
        perexod_igrok = self.browser.find_element(By.XPATH,'''//p[@class='se19-player-statistics__name']//a[contains(text(),"Джон Кордоба")]''')
        perexod_igrok.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/37436/seasons/2024-2025/', "Не правильный урл игрока"




