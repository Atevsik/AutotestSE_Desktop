from time import sleep
from selenium.webdriver.common.by import By


class ReviewsPage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/reviews/')
        sleep(6)

    def h1_rev(self):
        h1_news = self.browser.find_element(By.XPATH, '//h1[contains(text(),"Весь спорт.")]')

    def button_glvn_rev(self, count):
        button_glvn = self.browser.find_elements(By.XPATH, '//div[@class="se-material-list-filter__button-holder"]')
        assert len(button_glvn) == count

    def button_glvn_click_rev(self):
        button_glvn_click = self.browser.find_element(By.XPATH, '//a[contains(text(),"Главные")]')
        button_glvn_click.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/reviews/?isEditorialChoice=1', "Неверный урл Главные кнпк"

    def button_readers_rev(self):
        button_readers = self.browser.find_element(By.XPATH, '//a[contains(text(),"Выбор читателей")]')
        button_readers.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/reviews/?isHot=1', "Не верный урл Выбор читателей"

    def button_exclusive_rev(self):
        button_exclusive = self.browser.find_element(By.XPATH, '//a[contains(text(),"Эксклюзив")]')
        button_exclusive.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/reviews/?isExclusive=1', "Не верный урл кнопки эксклюз"

    def vid_materiala_button_rev(self):
        vid_materiala_button_rev = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter__top-left"]')

    def vid_sporta_button_rev(self):
        vid_sporta_button_rev = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter-menu"]')

    def hockey_button(self):
        hockey_button = self.browser.find_element(By.XPATH, '''//a[contains(@class,'se-material-filter-menu__item-button')][contains(text(),"Хоккей")]''')
        hockey_button.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/reviews/', "OSHIBKA УРЛА"

    def hocckey_page_rev(self):
        hocckey_page_rev = self.browser.find_element(By.XPATH,'//div[@class="se-press-list-page__items"]')


