from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class TennisRaiting:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/tennis/L/rates/atp/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def vibor(self):
        vibor = self.browser.find_element(By.XPATH,"//select[@id='champselect']")
        vibor.click()
        select = Select(vibor)
        select.select_by_index(1)
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/rates/wta/', "Не правильный урл"

    def vivod(self):
        vivod = self.browser.find_element(By.XPATH,"//div[@id='artbody']")






