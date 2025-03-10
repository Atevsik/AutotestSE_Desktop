from selenium.webdriver.common.by import By
from pages.newspage import NewsPage

def test_newspage(browser):
    newspage = NewsPage(browser)
    newspage.open()
    newspage.logo_news()
    newspage.button_glvn(3)
    newspage.button_glvn_click()
    newspage.button_exclusive()
    newspage.button_readers()
    newspage.vid_materiala_button()
    newspage.vid_sporta_button()
    newspage.football_button()
    newspage.h1_footbal_news()
    newspage.spisok_materialov()
    newspage.cup_selector()
    newspage.calendar_footbal()

