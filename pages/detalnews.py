from selenium.webdriver.common.by import By
from time import sleep

class DetalNews:

    def __init__(self, browser):
        self.browser = browser


    def open_detal_news(self):
        self.browser.get('https://www.sport-express.ru/football/rfpl/news/eks-prezident-lokomotiva-naumov-ocenil-igru-dzyuby-i-suleymanova-2188563/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def polog_comand(self):
        polog_comand = self.browser.find_element(By.XPATH, '//div[contains(text(),"Положение команд")]')

    def polog_comand1(self):
        polog_comand1 = self.browser.find_element(By.XPATH, '//tbody/tr[6]/td[1]/div[1]')

    def right_news(self):
        right_news = self.browser.find_element(By.XPATH, '//div[contains(text(),"Новости")]')

    def samie_obsyj(self):
        samie_obsyj = self.browser.find_element(By.XPATH, '//div[@class="se-readers-choice se-readers-choice--theme-detail"]')

    def podval(self):
        podval = self.browser.find_element(By.XPATH, '//footer[@class="se-footer"]')

    def perexod_table(self):
        perexod_table = self.browser.find_element(By.XPATH,'''//a[@class='se-menu-subtop__link'][contains(text(),"Таблица переходов")]''')
        perexod_table.click()
        sleep(3)
        assert self.browser.current_url == 'https://www.sport-express.ru/football/rfpl/reviews/rpl-tablica-perehodov-2024-2025-vse-transfery-kto-ushel-i-prishel-zenit-krasnodar-dinamo-lokomotiv-spartak-cska-sdelki-onlayn-2282277/' , "Не правильный урл"

    def perexod(self):
        perexod = self.browser.find_element(By.XPATH,'//tr[@id="himki-mo"]//td')

    def block_comment(self):
        block_comment = self.browser.find_element(By.XPATH, '//div[@class="smi-widget21682"]')
        block_comment = self.browser.execute_script("arguments[0].scrollIntoView();", block_comment)
        sleep(5)

    def block_commetn_click(self):
        block_comment_click = self.browser.find_element(By.XPATH, '//span[contains(text(),"Еще комментарии")]')
        block_comment_click.click()
