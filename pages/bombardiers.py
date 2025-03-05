from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Bombardiers:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/first/2023-2024/statistics/bombardiers/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def filtri(self):
        filtri = self.browser.find_element(By.XPATH,"//div[@class='se19-select-wr mb_20']")

    def top3(self,count):
        top3 = self.browser.find_elements(By.XPATH,"//div[@class='se19-players-statistics__player se19-player-statistics']")
        assert len(top3) == count

    def player(self):
        player = self.browser.find_element(By.XPATH,'''//p[@class='se19-player-statistics__name']//a[contains(text(),"Джонатан Окоронкво")]''')
        player.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/69429/seasons/2024-2025/', "Не правильный урл игрока"
        self.browser.back()

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")






