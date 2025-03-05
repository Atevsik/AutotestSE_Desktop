from selenium.webdriver.common.by import By
from time import sleep

class PhotoPage:

    def __init__(self, browser):
        self.browser = browser


    def open_photo(self):
        self.browser.get('https://www.sport-express.ru/photoreports/')

    def h1_news_photo(self):
        h1_news_photo = self.browser.find_element(By.XPATH, '//h1[contains(text(),"Весь спорт.")]')

    def button_photo(self, count):
        button_photo = self.browser.find_elements(By.XPATH, '//div[@class="se-material-list-filter__button-holder"]')
        assert len(button_photo) == count

    def button_photo_click(self):
        button_photo_click = self.browser.find_element(By.XPATH, '//div[@class="se-material-list-filter__bottom-left"]')

    def vid_materiala_button_photo(self):
        vid_materiala_button_photo = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter__top-left"]')

    def vid_sporta_button_photo(self):
        vid_sporta_button_photo = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter-menu"]')

    def fig_button(self):
        fig_button = self.browser.find_element(By.XPATH, '''//a[contains(@class,'se-material-filter-menu__item-button')][contains(text(),"Фигурное катание")]''')
        fig_button.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/figure-skating/photoreports/', "OSHIBKA УРЛА"