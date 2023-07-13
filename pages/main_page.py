import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    url = 'https://www.citilink.ru/'

    burger_menu = "//*[@id='__next']/div/header/div[1]/div[2]/div/button[1]"
    burger_menu_cities = "//button[@data-meta-name='MobileMenu__city-change-button']"
    select_cities = "//a[@data-meta-name='CitiesItem_Санкт-Петербург']"
    select_notebook = "//*[@id='__next']/div/main/div[1]/div[1]/div/div[2]/div/div[2]/div/a[1]"
    word_main_page = "//*[@id='__next']/div/header/div[2]/div/div/div[2]/div[1]/button/span/span"


    # Getters
    def get_burger_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu)))

    def get_burger_menu_cities(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu_cities)))

    def get_select_cities(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cities)))

    def get_select_notebook(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_notebook)))

    def get_word_main_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_main_page)))


    # Actions
    def click_word_main_page(self):
        self.get_word_main_page().click()
        print('Click Word Main Page')


    def click_burger_menu(self):
        self.get_burger_menu().click()
        print('Click Burger Menu')

    def click_burger_menu_cities(self):
        self.get_burger_menu_cities().click()
        print('Click Burger Menu Cities')

    def click_select_cities(self):
        self.get_select_cities().click()
        print('Click Select Cities')

    def click_select_notebook(self):
        self.get_select_notebook().click()
        print('Click Select Notebooks')

    # Methods
    def select_category(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.driver.fullscreen_window()
        self.assert_url("https://www.citilink.ru/")
        time.sleep(3)
        try:
            self.assert_text(self.get_word_main_page(), "Санкт-Петербург")
            self.click_select_notebook()
            time.sleep(3)
        except:
            self.driver.set_window_size(960,1080)
            self.click_burger_menu()
            self.click_burger_menu_cities()
            self.click_select_cities()
            self.click_select_notebook()
            time.sleep(3)

