from time import sleep
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/')
        sleep(6)

    def tablo_find(self):
        tablo_find = self.browser.find_element(By.CSS_SELECTOR, '.se-translation-scoreboard__events')

    def plitka(self):
        plitka = self.browser.find_element(By.CSS_SELECTOR, '.se-materials-grid-mosaic')

    def main_news(self):
        main_news = self.browser.find_element(By.CSS_SELECTOR, '''div[class='se-mainnews'] section[class='se-titled-block']''')

    def main_video(self):
        main_video = self.browser.find_element(By.XPATH, '//div[@class="se-video-block"]')

    def news(self):
        news = self.browser.find_element(By.XPATH, '//div[contains(text(),"Новости")]')

    def newspaper(self):
        newspaper = self.browser.find_element(By.XPATH, '//div[@class="se-slidertitled-block se-newspaper-widget-block"]')

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH, '//div[@class="se-articles-block"]')

    def readers(self):
        readers = self.browser.find_element(By.XPATH, '//div[@class="se-readers-choice se-readers-choice--theme-main"]')

    def photo_main(self):
        photo_main = self.browser.find_element(By.XPATH, '//div[@class="se-photoblock mb_40"]')

    def statblock_main(self):
        statblock_main = self.browser.find_element(By.XPATH, '//div[@class="se-statblock mb_20"]')

    def pollandteg_main(self, count):
        pollandteg_main = self.browser.find_elements(By.XPATH, '//section[@class="se-titled-block mb_30"]')  #Здесь два элемента проверяется опросы и теги
        assert len(pollandteg_main) == count

    def reklama_baner(self):
        reklama_banner = self.browser.find_element(By.XPATH,'//div[@id="adfox_15645683733586888"]')

