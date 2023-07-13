import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from faker import Faker
from pages.catalog_page import Catalog_page

fake = Faker(locale="ru_RU")

class Checkout_page(Base):

    # Globals
    price_to_checkout_page = '126 510'
    word_to_checkout_page = 'Ноутбук игровой ASUS TUF Gaming A17 FA707RM-HX031, 17.3", IPS, AMD Ryzen 7 6800HS, ' \
                            '8-ядерный, 16ГБ DDR5, 1ТБ SSD, NVIDIA GeForce RTX 3060 для ноутбуков - 6 ГБ, серый'

    # Locators
    checkout_price = "//*[@id='__next']/div/div[2]/div/div/div[2]/div[1]/span/span/span[1]"

    first_name = "//input[@name='contact-form_firstName']"
    last_name = "//input[@name='contact-form_lastName']"
    phone_number = "//input[@name='contact-form_phone']"
    store_selection_button = "//div[@class='css-0 ez87db90']"
    zoom_button = "// ymaps[@class='ymaps-2-1-79-zoom__plus ymaps-2-1-79-zoom__button ymaps-2-1-79-float-button ymaps-2-1-79-user-selection-none']"
    store_choice_button = "//*[@id='__next']/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div[3]/button"
    select_payment = "//*[text()='Банковской картой онлайн']"
    data_confirmation = "//input[@name='contactPaymentConfirm']"
    mail = "//input[@name='contactForCheck_email']"
    delete_button = "//div[@data-meta-name='DeleteAction']"
    main_page_button = "//a[@class='css-1k0cnlg e1mnvjgw0']"


    # Getters
    def get_checkout_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_price)))


    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_checkout_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_price)))

    def get_checkout_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_word)))

    def get_store_selection_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.store_selection_button)))

    def get_zoom_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zoom_button)))

    def get_store_choice_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.store_choice_button)))

    def get_scroll_to_sp(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_payment)))
    # если не кликается, то создать в base метод scroll
    def get_select_payment(self):
        self.driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_payment)))

    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_data_confirmation(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.data_confirmation)))

    def get_delete_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_button)))

    def get_main_page_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_page_button)))


    # Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Input first name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input last name')

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print('Input Phone Number')

    def click_store_selection_button(self):
        self.get_store_selection_button().click()
        print('Click Store Selection Button')

    def click_zoom_button(self):
        self.get_zoom_button().click()
        print('Click Zoom Button')
    #
    def click_store_choice_button(self):
        self.get_store_choice_button().click()
        print('Click Store Choice Button')

    def click_select_payment(self):
        self.get_select_payment().click()
        print('Click Select Payment')

    def click_data_confirmation(self):
        self.get_data_confirmation().click()
        print('Click Data Confirmation')
    #
    def input_mail(self, mail):
        self.get_mail().send_keys(mail)
        print('Input Mail')

    def click_delete_button(self):
        self.get_delete_button().click()
        print('Click Delete Button')

    def click_main_page_button(self):
        self.get_main_page_button().click()
        print('Click Main Page Button')

    def prices_catalog_page(self):
        price1 = self.get_catalog_price()
        global price_to_catalog_page
        price_to_catalog_page = price1.text
        return price_to_catalog_page

    def prices_checkout_page(self):
        price2 = self.get_checkout_price()
        global price_to_checkout_page
        price_to_checkout_page = price2.text
        return price_to_checkout_page


    # Methods
    def client_information(self):
        self.get_current_url()
        self.assert_url("https://www.citilink.ru/order/checkout/")
        self.get_screenshot()
        self.input_first_name(fake.first_name())
        self.input_last_name(fake.last_name())
        self.input_phone_number(fake.phone_number())
        self.assert_text(self.get_checkout_price(), '126 510')
        self.assert_price(Catalog_page.price_to_catalog_page, self.price_to_checkout_page)
        self.click_store_selection_button()
        self.click_zoom_button()
        self.click_store_choice_button()
        self.scroll_to_sp(self.get_scroll_to_sp())
        self.click_select_payment()
        self.input_mail(fake.email())
        self.click_data_confirmation()
        self.driver.back()
        self.click_delete_button()
        self.click_main_page_button()
        time.sleep(10)