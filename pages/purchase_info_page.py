import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base



class Purchase_info_page(Base):

    # Locators
    cart_button = "//*[text()='Перейти в корзину']"


    # Getters
    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))


    # Actions
    def click_cart_button(self):
        self.get_cart_button().click()
        print('Click Cart Button')


    # Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_cart_button()
