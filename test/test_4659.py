import logging

from selenium.webdriver.common.by import By
from pages.photopage import PhotoPage

def test_photopages(browser):
    photopage = PhotoPage(browser)
    photopage.open_photo()

    photo = photopage.h1_photo()
    assert photo is not None,"Заголовок не найден"
    logging.info("Заголовок ОК")

    poll = photopage.poll()
    assert poll is not None, "Опросы не найдены"
    logging.info("Опросы ОК")

    fig = photopage.fig()
    assert fig is not None, "Фигурное катание не найдено"
    logging.info("Фигурка ОК")

    photopage.reviews()
    assert photopage.reviews(expected_count=30), "Кол-во статей не соответствует ожидаемому"
    logging.info("Кол-во статей ОК")