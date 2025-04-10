from pages.tenismatch import TenisMatch
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_tenismatch(browser):
    tenismatch = TenisMatch(browser)
    tenismatch.open()
    tenismatch.menu_nadlogo()
    tenismatch.table()
    tenismatch.table2()
    #tenismatch.perexodturnir()
    tenismatch.selec()
    tenismatch.data()
