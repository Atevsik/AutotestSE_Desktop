from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class Stadion:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/hockey/L/khl/2023-2024/stadiums/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def name(self):
        name = self.browser.find_element(By.XPATH,"//a[contains(text(),'ВТБ Арена')]")

    def img(self):
        img = self.browser.find_element(By.XPATH,"//img[@title='Лада Арена']")

    def stadion(self):
        stadion = self.browser.find_element(By.XPATH,"//tbody/tr[20]/td[2]/a[1]")
        stadion.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/stadium/554/', "Не правильный урл стадиона"
        self.browser.back()

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Стадионы')]")

    def scrolsmi(self):
        scrolsmi = self.browser.find_element(By.XPATH,"//a[contains(text(),'ЦСКА Арена')]")
        scrolsmi = self.browser.execute_script("arguments[0].scrollIntoView();", scrolsmi)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@id='adfox_159523826122331374']")

