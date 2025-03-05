from selenium.webdriver.common.by import By
from time import sleep


class GlavnFootball:

    def __init__(self, browser):
        self.browser = browser

    def open_glavn_football(self):
        self.browser.get('https://www.sport-express.ru/football/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def plitka_glavn(self):
        plitka_glavn = self.browser.find_element(By.XPATH,"//div[@class='se-materials-grid-mosaic']")

    def glavn_news(self):
        glavn_news = self.browser.find_element(By.XPATH,'''//div[@class='se-mainnews']//section[@class="se-titled-block"]''')

    def news(self):
        news = self.browser.find_element(By.XPATH,'''//div[@class='se-newsline']//section[@class="se-titled-block"]''')

    def video(self):
        video = self.browser.find_element(By.XPATH, "//div[@class='se-video-block']")

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH, "//div[contains(text(),'Статьи')]")

    def poll(self):
        poll = self.browser.find_element(By.XPATH,"//section[@class='se-titled-block mb_30']")

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def result(self):
        result = self.browser.find_element(By.XPATH, '''//a[@class='se-menu-subtop__link'][contains(text(),"Результаты")]''')
        result.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/live/football/', "Не правильный урл, результаты"

    def title(self):
        title = self.browser.find_element(By.XPATH, "//div[@class='sp-sport-page__title']")

    def sport_navigator(self):
        sport_navigator = self.browser.find_element(By.XPATH,"//div[@class='se-sport-navigator']")

    def vid_materiala(self):
        vid_materiala = self.browser.find_element(By.XPATH,"//div[@class='swiper-wrapper']")

    def block_reklama(self):
        block_reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def bokmeker(self):
        bokmeker = self.browser.find_element(By.XPATH,"//div[@class='se-matchcenter-sports-list__extra']")

    def stavka(self):
        stavka = self.browser.find_element(By.XPATH,"//div[@class='se-matchcenter-match-extra__bets']")




