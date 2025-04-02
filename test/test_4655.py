import pytest
from selenium.webdriver.common.by import By
import time
from pages.homepage import HomePage
import logging

logging.basicConfig(level=logging.INFO)

def test_glavn_se(browser):
    homepage = HomePage(browser)
    homepage.open()

    tablo = homepage.tablo_find()
    assert tablo is not None, "Табло не найдено!"
    logging.info("Табло найдено - ОК")

    plitka = homepage.plitka()
    assert plitka is not None, "Блок с плиткой не найден"
    logging.info("Блок с плиткой найден - ОК")

    news_block = homepage.news()
    assert news_block is not None, "Блок с новостями не рнайден!"
    logging.info("Блок с новостями найден - ОК")

    homepage.check_metrika_console_events()

    main = homepage.main_news()
    assert main is not  None, "Блок главные новости не найден"
    logging.info("Главные новости - ОК")

    video = homepage.block_video()
    assert video is not None, "Блок видео не найден или не видим"
    logging.info("Блок видео - ОК")

    click = homepage.click_video()
    assert click is not None, "Клик не был совершен, либо кнопка не найдена"
    logging.info("Кнопка больше видео - ОК")

    reviews = homepage.block_reviews()
    assert reviews is not None, "Блок статьи не найден"
    logging.info("Блок статьи - ОК")

    reads = homepage.read()
    assert reads is not None, "Блок выбор читателей не найден"
    logging.info("Блок выбор читателей - ОК")

    photo = homepage.block_photo()
    assert photo is not None, "Блок фото не найден"
    logging.info("Блок фото - ОК")

    reklama = homepage.block_reklama()
    assert reklama is not None, "Блок с рекламой не найден"
    logging.info("Блок реклама - ОК")

    comand = homepage.block_table()
    assert comand is not None, "Блок с положением команд не найден"
    logging.info("Положение команд - ОК")

    stat = homepage.block_stat()
    assert stat is not None, "Блок статистике не найден"
    logging.info("Статистика - ОК")