from pages.treners import Trener
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_treners(browser):
    treners = Trener(browser)
    treners.open()
    treners.menu_nadlogo()
    treners.nikitin()
    treners.srloll()
    treners.knoka()
    treners.spisok(339)
    treners.knoka()
    treners.spisok(255)
    treners.h1()
    treners.reklama()
    treners.table()