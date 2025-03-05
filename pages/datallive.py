from selenium.webdriver.common.by import By
from time import sleep


class DetalLive:

    def __init__(self, browser):
        self.browser = browser

    def open_detal_live(self):
        self.browser.get('https://www.sport-express.ru/football/rfpl/online/spartak-fakel-smotret-besplatno-match-20-tura-rpl-v-pryamom-efire-onlayn-tekstovaya-translyaciya-i-rezultat-10-marta-2024-2187914/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def datelive(self):
        detelive = self.browser.find_element(By.XPATH, '//div[contains(text(),"10 марта, 21:03")]')

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def dopknopkalive(self):
        dopknopkalive = self.browser.find_element(By.XPATH,'//div[@class="se-menu-subtop__link"]')
        dopknopkalive.click()

    def videoclicklive(self):
        videoclicklive = self.browser.find_element(By.XPATH, '''//div[@class='se-menu-subtop-popup__link']//a[contains(text(),"Видео")]''')
        videoclicklive.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/rfpl/videoreports/', "Не правильный урл видео"

    def h1_video(self):
        h1_video = self.browser.find_element(By.XPATH, '//h1[contains(text(),"Видео: футбол РПЛ")]')

    def items_video(self):
        items_video = self.browser.find_element(By.XPATH, "//div[@class='se-video-list-page__items']")