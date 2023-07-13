import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Order_page(Base):

    # Locators
    order_button = "//*[text()='Перейти к оформлению']"
    url = "https://www.citilink.ru/order/"

    # Getters
    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    def get_url(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.url)))


    # Actions
    def click_order_button(self):
        self.get_order_button().click()
        print('Click Order Button')


    # Methods

    def order(self):

        self.get_current_url()
        self.click_order_button()
        self.get_screenshot()
        # self.assert_url('https://www.citilink.ru/order/')
