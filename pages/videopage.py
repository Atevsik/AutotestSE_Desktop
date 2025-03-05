from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VideoPage:

    def __init__(self, browser):
        self.browser = browser


    def open_video(self):
        self.browser.get('https://www.sport-express.ru/videoreports/')

    def h1_news_video(self):
        h1_news_video = self.browser.find_element(By.XPATH, '//h1[contains(text(),"Видео")]')

    def button_video(self, count):
        button_video = self.browser.find_elements(By.XPATH, '//div[@class="se-material-list-filter__button-holder"]')
        assert len(button_video) == count

    def button_video_click(self):
        button_video_click = self.browser.find_element(By.XPATH, '//a[contains(text(),"Главные")]')
        button_video_click.click()
        sleep(30)
        assert self.browser.current_url == 'https://www.sport-express.ru/videoreports/?isEditorialChoice=1', "Неверный урл Главные кнпк"

    def button_readers_video(self):
        button_readers_video = self.browser.find_element(By.XPATH, '//a[contains(text(),"Выбор читателей")]')
        button_readers_video.click()
        sleep(30)
        assert self.browser.current_url == 'https://www.sport-express.ru/videoreports/?isHot=1', "Не верный урл Выбор читателей"

    def button_exclusive_video(self):
        button_exclusive_video = self.browser.find_element(By.XPATH, '//a[contains(text(),"Эксклюзив")]')
        button_exclusive_video.click()
        sleep(30)
        assert self.browser.current_url == 'https://www.sport-express.ru/videoreports/?isExclusive=1', "Не верный урл кнопки эксклюз"

    def vid_materiala_button_vid(self):
        vid_materiala_button_vid = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter__top-left"]')

    def vid_sporta_button_vid(self):
        vid_sporta_button_vid = self.browser.find_elements(By.XPATH, '//div[@class="se-material-filter-menu"]')

    def mma_button(self):
        mma_button = self.browser.find_element(By.XPATH, '''//a[contains(@class,'se-material-filter-menu__item-button')][contains(text(),"Бокс/ММА")]''')
        mma_button.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/martial/videoreports/', "OSHIBKA УРЛА"