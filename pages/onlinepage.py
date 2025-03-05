from selenium.webdriver.common.by import By
from time import sleep

class OnlinePage:

    def __init__(self, browser):
        self.browser = browser


    def open_online(self):
        self.browser.get('https://www.sport-express.ru/online/')

    def h1_news_online(self):
        h1_news_online = self.browser.find_element(By.XPATH, '//h1[contains(text(),"Весь спорт.")]')

    def button_online(self, count):
        button_online = self.browser.find_elements(By.XPATH, '//div[@class="se-material-list-filter__button-holder"]')
        assert len(button_online) == count

    def button_photo_online(self):
        button_photo_online = self.browser.find_element(By.XPATH, '//div[@class="se-material-list-filter__bottom-left"]')

    def vid_materiala_button_online(self):
        vid_materiala_button_online = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter__top-left"]')

    def vid_sporta_button_online(self):
        vid_sporta_button_online = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter-menu"]')

    def knopka_eshe_online(self):
        knopka_eshe_online = self.browser.find_element(By.XPATH, '//div[@class="se-material-filter-menu__item-button "]')

    def knopka_eshe_online_click(self):
        knopka_eshe_online_click = self.browser.find_element(By.XPATH,'//a[@href="/tennis/online/"]')
        knopka_eshe_online_click.click()

    def materials_tenis_online(self):
        materials_tenis_online = self.browser.find_element(By.XPATH, '//div[@class="se-online-list-page__items"]')
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/online/', "Не правильынй урл"

    def pokazat_online(self):
        pokazat_online = self.browser.find_element(By.XPATH, '//a[contains(text(),"Показать еще")]')
        pokazat_online.click()
