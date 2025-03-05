from selenium.webdriver.common.by import By
from time import sleep

class NewsPhoto:

    def __init__(self, browser):
        self.browser = browser


    def open_photo_news(self):
        self.browser.get('https://www.sport-express.ru/football/rfpl/photoreports/spartak-proigral-fakelu-v-matche-rpl-v-luzhnikah-foto-igry-10-marta-2024-2188299/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def comento_scroll(self):
        comento_scroll = self.browser.find_element(By.XPATH, '//div[contains(text(),"Результаты / календарь")]')
        comento_scroll = self.browser.execute_script("arguments[0].scrollIntoView();", comento_scroll)
        sleep(7)

    def commento_check(self):
        commento_check = self.browser.find_element(By.XPATH,'//span[contains(text(),"Еще комментарии")]')
        commento_check.click()
        sleep(4)

    def commento_check_newComment(self):
        commento_check_newComment = self.browser.find_element(By.XPATH, '//div[@id="comment-text-12590332"]')

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def click_statistik(self):
        click_statistik = self.browser.find_element(By.XPATH, '''//a[@class='se-menu-subtop__link'][contains(text(),"Статистика")]''')
        click_statistik.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/russia/premier/2024-2025/statistics/bombardiers/', "не правильный урл статистики "

    def statistik_select(self):
        statistik_select = self.browser.find_element(By.XPATH, '//div[@class="se19-select-wr mb_20"]')

    def igrok_statistik(self):
        igrok_statistik = self.browser.find_element(By.XPATH, '//a[contains(text(),"Константин Савичев")]')

    def top3(self, count):
        top3 = self.browser.find_elements(By.XPATH, '//div[@class="se19-players-statistics__player se19-player-statistics"]')
        assert len(top3) == count




