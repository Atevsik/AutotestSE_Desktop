import logging

from selenium.webdriver.common.by import By
from pages.videopage import VideoPage
from time import sleep

def test_videopage(browser):
    videopage = VideoPage(browser)
    videopage.open_video()

    h1 = videopage.h1_video()
    assert h1 is not None,"Заголовок не найден"
    logging.info("Заголовок ОК")

    button1 = videopage.button_main()
    assert button1 is not None, "Кнопка Главная не найдена"
    logging.info("Кнопка ОК ")

    button2 = videopage.button_readers()
    assert button2 is not None, "Кнопка Читатели не найдена"
    logging.info("Кнопка ОК ")

    button3 = videopage.button_exclusive()
    assert button3 is not None, "Кнопка Эксклюзив не найдена"
    logging.info("Кнопка ОК ")

    back = videopage.back()
    assert back is not None, "Кнопка весь спорт не найдена"
    logging.info("Кнопка ОК")

    reklama = videopage.reklama()
    assert reklama is not None,"Реклама не найдена"
    logging.info("Реклама ОК")

    story = videopage.story()
    assert story is not None,"Сюжеты не найдены"
    logging.info("Сюжеты ОК")