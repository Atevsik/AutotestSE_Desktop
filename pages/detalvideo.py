from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class DetalVideo:

    def __init__(self, browser):
        self.browser = browser

    def open_detal_video(self):
        self.browser.get('https://www.sport-express.ru/hockey/khl/videoreports/aleksandr-hmelevskiy-vylet-salavata-seriya-s-traktorom-buduschee-v-klube-intervyu-2188513/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def eshe(self):
        eshe = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop__link"]')
        eshe.click()

    def perexod_stadium(self):
        perexod_stadium = self.browser.find_element(By.XPATH,'''//div[@class='se-menu-subtop-popup__link']//a[contains(text(),"Стадионы")]''')
        perexod_stadium.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/khl/2024-2025/stadiums/', "Не правильный урл стадиона"

    def table_stadium(self):
        table_staium = self.browser.find_element(By.XPATH, '//div[@class="sp-page sp-page--overflow"]')

    def stadium_click(self):
        stadium_click = self.browser.find_element(By.XPATH, '//tbody/tr[7]/td[2]')
        stadium_click.click()

    def tag_stadium_check(self):
        tag_stadium_check = self.browser.find_element(By.XPATH, '//div[@class="sp-profile-name__name"]')
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/stadium/452/'

    def h1_stadium(self):
        h1_stadium = self.browser.find_element(By.XPATH, '//h1[contains(text(),"Стадионы")]')


