from pages.tagcomands import TagComand
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_tagcomand(browser):
    tagcomand = TagComand(browser)
    tagcomand.open()
    tagcomand.menu_nadlogo()
    tagcomand.info_comand(6)
    tagcomand.material()
    tagcomand.sostav()
    tagcomand.igroki(3)
    tagcomand.click_igrok()
    tagcomand.raspisanie()
    tagcomand.raspisanie2()
    #tagcomand.srlollsmi()
    #tagcomand.smi2()
    tagcomand.statistik_player()
    #tagcomand.info_stat(781)
    tagcomand.polevie()
    tagcomand.vratari()
    tagcomand.zash()
    tagcomand.napad()
    tagcomand.stat_comand()
    #tagcomand.stat_info()
    #tagcomand.click()
    tagcomand.treneri()
    tagcomand.starica()
    tagcomand.raspisanie()
    tagcomand.raspisan()
    tagcomand.soper()
    tagcomand.vragi()
    tagcomand.istoria_vstr(35)
    tagcomand.istoria_vstr2()
# Вернусь в новой версии, сделаем красиво, временый костыль
