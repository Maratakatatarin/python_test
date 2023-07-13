# -*- coding: utf8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.catalog_page import Catalog_page
from pages.info_notebook_page import Info_notebook_page
from pages.main_page import Main_page
from pages.checkout_page import Checkout_page
from pages.order_page import Order_page


def test_buy_notebook(set_up):
    # чтобы в терминале не показывало ничего лишнего см. https://yandex.ru/video/preview/14751657242096540528,
    # затем пишем две нижние строчки с "options", затем добавляем "chrome_options=options" в "g = Service"
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    # переместили файл chromedriver.exe в C:\Users\user\PycharmProjects\pythonLessons\resource, файл используется один для всех проектов
    # но можно использовать просто "g = Service()"
    g = Service(executable_path='/resource/chromedriver.exe', chrome_options=options)
    driver = webdriver.Chrome(options=options, service=g)

    mp = Main_page(driver)
    mp.select_category()

    cp = Catalog_page(driver)
    cp.select_notebooks()

    inp = Info_notebook_page(driver)
    inp.info()

    op = Order_page(driver)
    op.order()

    chp = Checkout_page(driver)
    chp.client_information()
    time.sleep(5)

