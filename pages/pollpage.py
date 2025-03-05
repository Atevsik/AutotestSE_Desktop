from selenium.webdriver.common.by import By
from time import sleep

class PollPage:

    def __init__(self, browser):
        self.browser = browser


    def open_poll(self):
        self.browser.get('https://www.sport-express.ru/poll/')

    def h1_news_poll(self):
        h1_news_poll = self.browser.find_element(By.XPATH, '//h1[contains(text(),"Весь спорт.")]')

    def button_poll(self, count):
        button_poll = self.browser.find_elements(By.XPATH, '//div[@class="se-material-list-filter__button-holder"]')
        assert len(button_poll) == count

    def button_photo_poll(self):
        button_photo_poll = self.browser.find_element(By.XPATH, '//div[@class="se-material-list-filter__bottom-left"]')

    def vid_materiala_button_poll(self):
        vid_materiala_button_poll = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter__top-left"]')

    def vid_sporta_button_poll(self):
        vid_sporta_button_poll = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter-menu"]')

    def knopka_eshe_poll(self):
        knopka_eshe_online = self.browser.find_element(By.XPATH, '//div[@class="se-material-filter-menu__item-button "]')
        knopka_eshe_online.click()

    def knopka_eshe_poll_click(self):
        knopka_eshe_poll_click = self.browser.find_element(By.XPATH,'//a[@href="/volleyball/poll/"]')
        knopka_eshe_poll_click.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/volleyball/poll/', "Не правильынй урл"


