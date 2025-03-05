from selenium.webdriver.common.by import By
from time import sleep

class DetalReviews:

    def __init__(self, browser):
        self.browser = browser

    def open_detal_reviews(self):
        self.browser.get('https://www.sport-express.ru/football/rfpl/reviews/lokomotiv-sygral-vnichyu-s-sochi-mnenie-byvshego-prezidenta-zheleznodorozhnikov-nikolaya-naumova-o-matche-2188444/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def tegi(self, count):
        tegi = self.browser.find_elements(By.XPATH, '//span[@class="se-tag__name"]')
        assert len(tegi) == count

    def like_dis(self):
        like_dis = self.browser.find_element(By.XPATH, '//div[@class="se-material-user-actions-rows"]')

    def podelit(self):
        podelit = self.browser.find_element(By.XPATH, '//div[@class="se-shareblock se-material-user-actions-rows__share se-shareblock--popup-rows se-shareblock--popup"]')
        podelit.click()

    def proverka_podelit(self, count):
        proverka_podelit = self.browser.find_elements(By.XPATH,'//button[@class="react-share__ShareButton"]')
        assert len(proverka_podelit) == count

    def perexod_calendar(self):
        perexod_calendar = self.browser.find_element(By.XPATH,'''//a[@class='se-menu-subtop__link'][contains(text(),"Календарь")]''')
        perexod_calendar.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/russia/premier/2024-2025/calendar/tours/', "Не правильный урл календаря"

    def selector_season(self):
        selector_season = self.browser.find_element(By.XPATH, '//div[@class="se19-select-wr mb_20"]')

    def tour(self):
        tour = self.browser.find_element(By.XPATH,'//tbody/tr[28]/th[1]')