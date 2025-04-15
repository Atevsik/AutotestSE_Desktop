from pages.comandsdiviz import ComandDiviz
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_comanddiviz(browser):
    comanddiviz = ComandDiviz(browser)
    comanddiviz.open()
    comanddiviz.menu_nadlogo()
    #comanddiviz.deviz(4)
    comanddiviz.knopki()
    comanddiviz.spartak()
    comanddiviz.filtri()
