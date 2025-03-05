from selenium.webdriver.common.by import By
from time import sleep

class StoryPage:

    def __init__(self, browser):
        self.browser = browser


    def open_story(self):
        self.browser.get('https://www.sport-express.ru/stories/')

    def h1_news_story(self):
        h1_news_story = self.browser.find_element(By.XPATH, '//h1[contains(text(),"Весь спорт.")]')

    def button_story(self, count):
        button_story = self.browser.find_elements(By.XPATH, '//div[@class="se-material-list-filter__button-holder"]')
        assert len(button_story) == count

    def button_story_click(self):
        button_story_click = self.browser.find_element(By.XPATH, '//div[@class="se-material-list-filter__bottom-left"]')

    def vid_materiala_button_story(self):
        vid_materiala_button_story = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter__top-left"]')

    def vid_sporta_button_story(self):
        vid_sporta_button_story = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter-menu"]')

    def bask_button(self):
        bask_button = self.browser.find_element(By.XPATH, '''//a[contains(@class,'se-material-filter-menu__item-button')][contains(text(),"Баскетбол")]''')
        bask_button.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/basketball/stories/', "OSHIBKA УРЛА"

    def button_nextpage(self):
        button_nextpage = self.browser.find_element(By.XPATH,'//a[contains(text(),"Показать еще")]')
        button_nextpage.click()