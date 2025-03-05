from time import sleep
from selenium.webdriver.common.by import By

class NewsPage:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/news/')

    def logo_news(self):
        logo_news = self.browser.find_element(By.XPATH, '//div[@class="se-logo"]')

    def h1_news(self):
        h1_news = self.browser.find_element(By.XPATH, '//h1[contains(text(),"Весь спорт.")]')

    def button_glvn(self, count):
        button_glvn = self.browser.find_elements(By.XPATH, '//div[@class="se-material-list-filter__button-holder"]')
        assert len(button_glvn) == count

    def button_glvn_click(self):
        button_glvn_click = self.browser.find_element(By.XPATH, '//a[contains(text(),"Главные")]')
        button_glvn_click.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/news/?isEditorialChoice=1', "Неверный урл Главные кнпк"

    def button_readers(self):
        button_readers = self.browser.find_element(By.XPATH, '//a[contains(text(),"Выбор читателей")]')
        button_readers.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/news/?isHot=1', "Не верный урл Выбор читателей"

    def button_exclusive(self):
        button_exclusive = self.browser.find_element(By.XPATH, '//a[contains(text(),"Эксклюзив")]')
        button_exclusive.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/news/?isExclusive=1', "Не верный урл кнопки эксклюз"


    def vid_materiala_button(self):
        vid_materiala_button = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter__top-left"]')

    def vid_sporta_button(self):
        vid_sporta_button = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter-menu"]')

    def football_button(self):
        football_button = self.browser.find_element(By.XPATH,'''//a[contains(@class,'se-material-filter-menu__item-button')][contains(text(),"Футбол")]''')
        football_button.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/news/', "OSHIBKA УРЛА"

    def subckribe_block(self):
        subckribe_block = self.browser.find_element(By.XPATH,'//div[@class="se-subscribe-block"]')

    def h1_footbal_news(self):
        h1_footbal_news = self.browser.find_element(By.XPATH,'//h1[contains(text(),"Новости футбола")]')

    def spisok_materialov(self):
        spisok_materialov = self.browser.find_element(By.XPATH, '//div[@class="se-news-list-page__items"]')

    def cup_selector(self):
        cup_selector_click = self.browser.find_element(By.XPATH, '//div[@class="se-select se-select--1col se-select--selected se-select--theme-sky"]')
        cup_selector_click.click()

    def cup_selector_click(self):
        cup_selector_click = self.browser.find_element(By.XPATH, '//div[@class="se-select__item"][7]')
        cup_selector_click.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/world/news/'

    def calendar_footbal(self):
        calendar_footbal = self.browser.find_element(By.XPATH, '//div[@class="se-calendar-button"]')
        calendar_footbal.click()

    def calendar_footbal_click(self):
        calendar_footbal_click = self.browser.find_element(By.XPATH, '//abbr[@aria-label="17 декабря 2024 г."]')
        calendar_footbal_click.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/world/news/?publicationDate=17.12.2024'