from selenium.webdriver.common.by import By
from time import sleep


class DetalStory:

    def __init__(self, browser):
        self.browser = browser

    def open_detal_story(self):
        self.browser.get('https://www.sport-express.ru/football/rus_cup/stories/kubok-rossii-pley-off-puti-rpl-i-regionov-1-4-finala-1-2-i-final-zherebevka-pary-i-rezultaty-matchey-2023-2024-2140252/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def block_reviews(self):
        block_reviews = self.browser.find_element(By.XPATH, '//div[@class="se-material-page"]//div[1]//section[1]')

    def block_news(self):
        block_news = self.browser.find_element(By.XPATH, '//div[@class="se-grid2col__left"]//div[2]//section[1]')

    def block_video(self):
        block_video = self.browser.find_element(By.XPATH,'//div[@class="se-material-page__footer-stories"]//div[3]//section[1]')

    def block_photo(self):
        block_photo = self.browser.find_element(By.XPATH, '//div[@class="se-material-page__footer"]//div[4]//section[1]')

    def rev_knp(self,count):
        rev_knp = self.browser.find_elements(By.XPATH,'//a[@class="se-button se-button--size-middle more_button"][1]')
        assert len(rev_knp) == count

    def click_knp(self):
        click_knp = self.browser.find_element(By.XPATH,'//a[@class="se-button se-button--size-middle more_button"][1]')
        click_knp.click()

    def calendar_nad_menu(self):
        calendar_nad_menu = self.browser.find_element(By.XPATH,'''//a[@class='se-menu-subtop__link'][contains(text(),"Календарь")]''')
        calendar_nad_menu.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/russia/cup/2024-2025/calendar/tours/', "Не правильный урл календаря"

    def h1_calend_det(self):
        h1_calen_det = self.browser.find_element(By.XPATH,'//h1[contains(text(),"FONBET Кубок России 2024-2025, расписание матчей, ")]')

    def filtri(self):
        filtri = self.browser.find_element(By.XPATH,'//div[@class="se19-select-wr mb_20"]')

    def click_match(self):
        click_match = self.browser.find_element(By.XPATH,'//tbody/tr[2]/td[3]/div[1]/p[1]/a[1]')
        click_match.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/rus_cup/fbl_match-spartak-dinamo-399751/', "Не правильный матч"

