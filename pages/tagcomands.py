from itertools import count

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class TagComand:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, "//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def info_comand(self,count):
        info_comand = self.browser.find_elements(By.XPATH,"//div[@class='sp-param-list__item-value']")
        assert len(info_comand) == count

    def material(self):
        material = self.browser.find_element(By.XPATH,"//div[@class='se-page-filters se-page-filters--size-sm se-tag-profile-materials-filter']")

    def knopka(self):
        knopka = self.browser.find_element(By.XPATH,"//div[@class='se-button se-button--size-big']")
        knopka.click()
        sleep(2)
        knopka = self.browser.execute_script("arguments[0].scrollIntoView();", knopka)


    def sostav(self):
        sostav = self.browser.find_element(By.XPATH,"//a[contains(text(),'Состав')]")
        sostav.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/players/', "Не правильная ссылка состава"

    def igroki(self,count):
        igroki = self.browser.find_elements(By.XPATH,"//div[@class='sp-team-composition__group']")
        assert len(igroki) == count

    def click_igrok(self):
        click_igrok = self.browser.find_element(By.XPATH,"//body[1]/div[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/a[1]")
        click_igrok.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/hockey/L/player/10621/', "Не правильный урл тега"
        self.browser.back()

    def raspisanie(self):
        raspisanie = self.browser.find_element(By.XPATH,"//a[contains(text(),'Расписание')]")
        raspisanie.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/schedule/', "Не правлиьный урл расписания"

    def raspisanie2(self):
        raspisanie2 = self.browser.find_element(By.XPATH,"//div[@class='sp-page']")

    def srlollsmi(self):
        scrlolsmi = self.browser.find_element(By.XPATH,"//td[normalize-space()='22.03.2025']")
        scrlolsmi =  self.browser.execute_script("arguments[0].scrollIntoView();", scrlolsmi)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@class='sp-banner']")

    def statistik_player(self):
        statistik_player = self.browser.find_element(By.XPATH,"//a[contains(text(),'Статистика игроков')]")
        statistik_player.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/players-stats/', "Не правильный урл статистики"

    def info_stat(self,count):
        info_stat = self.browser.find_elements(By.XPATH,"//td[@class='se-advanced-table-cell']")
        assert len(info_stat) == count

    def polevie(self):
        polevie = self.browser.find_element(By.XPATH,"//div[contains(text(),'Полевые игроки')]")
        polevie.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/players-stats/?stage=undefined&role=outfields', "Не правильные полевые"

    def vratari(self):
        vratari = self.browser.find_element(By.XPATH,"//div[contains(text(),'Вратари')]")
        vratari.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/players-stats/?stage=undefined&role=goalkeeper',"Не правильные вратари"

    def zash(self):
        zash = self.browser.find_element(By.XPATH,"//div[contains(text(),'Защитники')]")
        zash.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/players-stats/?stage=undefined&role=defense', "Не правльные защитники"

    def napad(self):
        napad = self.browser.find_element(By.XPATH,"//div[contains(text(),'Нападающие')]")
        napad.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/players-stats/?stage=undefined&role=forward', "Не правлиьные нападающие"

    def stat_comand(self):
        stat_comand = self.browser.find_element(By.XPATH,"//a[contains(text(),'Статистика команды')]")
        stat_comand.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/stats/', "Не правильная статистика команды"

    def stat_info(self):
        stat_info = self.browser.find_element(By.XPATH,"//div[@class='sp-page sp-page--overflow']")

    def click(self):
        click = self.browser.find_element(By.XPATH,"//body[1]/div[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]")
        click.click()

    def treneri(self):
        treneri = self.browser.find_element(By.XPATH,"//div[@class='se-page-menu-item']//a[contains(text(),'Тренеры')]")
        treneri.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/trainers/', "Не правильные теренры"

    def starica(self):
        stranica = self.browser.find_element(By.XPATH,"//div[@class='sp-page sp-page--overflow']")

    def raspisan(self):
        raspisan = self.browser.find_element(By.XPATH,"//div[@class='se-titled-block__title se-titled-block__title--fs-md']")

    def soper(self):
        soper = self.browser.find_element(By.XPATH,"//a[contains(text(),'Соперники')]")
        soper.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/competitor/', "Не правильные теренры"

    def vragi(self):
        vragi = self.browser.find_element(By.XPATH,"//div[@class='sp-page sp-page--overflow']")

    def istoria_vstr(self,count):
        isoria_vstr = self.browser.find_elements(By.XPATH,"(//a[contains(text(),'История встреч')])")
        assert len(isoria_vstr) == count

    def istoria_vstr2(self):
        isoria_vstr2 = self.browser.find_element(By.XPATH,"(//a[contains(text(),'История встреч')])[8]")
        isoria_vstr2.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tag/metallurg-mg-hokkey-270/competitor/12/', "не правильная история встреч"


