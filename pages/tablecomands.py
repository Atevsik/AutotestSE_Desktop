from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TableComands:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/premier/2024-2025/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Россия. Премьер-лига 2024-2025, турнирные таблицы')]")

    def legend(self):
        legend = self.browser.find_element(By.XPATH,"//div[@class='table-color-legend']")

    def table_comands(self):
        table_comands = self.browser.find_element(By.XPATH,"//div[@class='tournir_table strong_border']")

    def spartak(self):
        spartak = self.browser.find_element(By.XPATH,"(//a[contains(text(),'Спартак')])[2]")
        spartak.click()
        sleep(5)
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/command/1/', "Не правильный урл спартака"






