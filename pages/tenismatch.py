from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class TenisMatch:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/tennis/L/atp/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def table(self):
        table = self.browser.find_element(By.XPATH,"//div[@id='artbody']")

    def table2(self):
        table2 = self.browser.find_element(By.XPATH,"//tbody/tr[25]/td[2]")

    def perexodturnir(self):
        perexodturnir = self.browser.find_element(By.XPATH,"//tbody/tr[6]/td[2]/a[1]")
        perexodturnir.click()
        sleep(5)
        assert self.browser.current_url == "https://www.sport-express.ru/tennis/L/atp/adelaide/2025/", 'Не правильный урл турнира'
        self.browser.back()

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_159523747962947596']")

    def selec(self):
        selec = self.browser.find_element(By.XPATH,"//div[@id='artbody']/select")
        selec.click()
        select = Select(selec)
        select.select_by_index(2)
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/atp/2023/', "Не правильный год"

    def data(self):
        data = self.browser.find_element(By.XPATH,"//td[normalize-space()='09.01.2023 - 14.01.2023']")






