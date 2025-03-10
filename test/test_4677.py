from pages.tablecomands import TableComands
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_tablecomands(browser):
    tablecomands = TableComands(browser)
    tablecomands.open()
    tablecomands.h1()
    tablecomands.legend()
    tablecomands.table_comands()