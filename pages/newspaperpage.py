from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class PaperGazeta:

    def __init__(self, browser):
        self.browser = browser


    def open_gazeta(self):
        self.browser.get('https://www.sport-express.ru/newspaper/')

    def calendar_gazet(self):
        calendar_gazet = self.browser.find_element(By.XPATH, '//span[@id="calendar_icon"]')
        calendar_gazet.click()

    def calendar_gazet_prov(self):
        calendar_gazet_prov = self.browser.find_element(By.XPATH, '//div[@id="ui-datepicker-div"]')

    def filtr_gaz(self):
        filtr_gaz = self.browser.find_element(By.XPATH, '//div[@class="se19-rubricator__group"][1]')

    def vid_sporta_gaz(self):
        vid_sporta_gaz = self.browser.find_element(By.XPATH, '//div[@class="se19-rubricator"]')
        vid_sporta_gaz.click()

    def proverka_Vid_sporta(self):
        proverka_Vid_sporta = self.browser.find_element(By.XPATH, '//div[@id="se-newspaper-content"]')
