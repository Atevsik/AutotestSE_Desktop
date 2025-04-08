from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class PaperGazeta:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)
        self.original_window = None

    def open_gazeta(self):
        self.browser.get('https://www.sport-express.ru/newspaper/')

    def calendar(self):
        try:
            calendar = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,'//span[@id="calendar_icon"]')))
            logging.info("Кнопка календаря найдена")
            calendar.click()
            sleep(3)
            return calendar
        except TimeoutException:
            logging.info("Кнопка календаря не найдена")
            return None

    def proverka(self):
        try:
            proverka = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[@id='ui-datepicker-div']")))
            logging.info("Календарь отображается")
            return proverka
        except TimeoutException:
            return None

    def reklama(self):
        try:
            reklama = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='adfox_1479211722']")))
            logging.info("Реклама отображается")
            return reklama
        except TimeoutException:
            return None


    def polosi(self):
        try:
            polosi = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Полоса 1')]")))
            logging.info("Полосы отображаются")
            return polosi
        except TimeoutException:
            return None