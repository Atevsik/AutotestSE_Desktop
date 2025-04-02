from selenium.webdriver.common.by import By
from pages.newspage import NewsPage
import logging

def test_newspage(browser):
    newspage = NewsPage(browser)
    newspage.open()

    h1 = newspage.h1_news()
    assert h1 is not None, "Заголовок не найден"
    logging.info("Заголовок ОК")

    button1 = newspage.button_main()
    assert button1 is not None,"Кнопка Главная не найдена"
    logging.info("Кнопка ОК ")

    button2 = newspage.button_readers()
    assert button2 is not None,"Кнопка Читатели не найдена"
    logging.info("Кнопка ОК ")

    button3 = newspage.button_exclusive()
    assert button3 is not None,"Кнопка Эксклюзив не найдена"
    logging.info("Кнопка ОК ")

    reviews = newspage.reviews_vid()
    assert reviews is not None,"Кнопка не найдена"
    logging.info("Кнопка ОК")

    football = newspage.football_button()
    assert football is not None, "Кнопка Футбол, не найдена"
    logging.info("Кнопка ОК")

    h1_football = newspage.h1_football_news()
    assert h1_football is not None,"Заголовок футбола не найден"
    logging.info("Заголовок ОК")

    newspage.reviews()
    assert newspage.reviews(expected_count=30), "Кол-во статей не соответствует ожидаемому"
    logging.info("Кол-во статей ОК")

    selector = newspage.cup_selector()
    assert selector is not None,"Слектор не найден"
    logging.info("Селкетор ОК")

    rpl = newspage.cup_rpl()
    assert rpl is not None,"РПЛ не найден"
    logging.info("РПЛ ОК")

    reklama = newspage.reklama_block()
    assert  reklama is not None, "Реклама не найдена"
    logging.info("Реклама ОК")