import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Catalog_page(Base):

    # Globals
    price_to_catalog_page = '126 510'
                            # 242 990
    # Locators
    catalog_price = "//span[text()='126 510']"
                    #//span[text()='242 990']

    filter_button = "//div[@class='app-catalog-ud6ms9 eyoh4ac0']"
    filter_price = "//div[@class='rc-slider rc-slider-horizontal']"
    choice_minPrice = "//input[@name='input-min']"
    choice_maxPrice = "//input[@name='input-max']"
    button_all = "//*[text()='Все']"
    checkbox_acer = "//input[@id='acer']"
    checkbox_asus = "//input[@id='asus']"
    checkbox_msi = "//input[@id='msi']"
    button_back = "/html/body/div[11]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]"
    screen_size_16 = """//button[text()='16 "']"""
    screen_size_17 = """//button[text()='17 "']"""
    button_video_memory6gb = "//button[@data-meta-value='6 ГБ']"
    button_show_results = "//div[@class='css-1xdhyk6 e1hnr9x50']"
    sort_button = "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[2]/div[1]/div[2]/div[1]"
    low_price = "//span[text()='по возрастанию цены']"
    add_to_cart = "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[3]/div/div[7]/div[2]"
                  #//*[@id="__next"]/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[10]/div/div[7]/div[2]


    # Getters
    def get_catalog_price(self):
        # self.driver.execute_script(  "var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_price)))

    def get_filter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_button)))

    def get_filter_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price)))

    def get_choice_minPrice(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choice_minPrice)))

    def get_button_all(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_all)))

    # чтобы кликнуть на checkbox, вместо "EC.element_to_be_clickable" нужно писать "EC.presence_of_element_located"
    def get_checkbox_acer(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.checkbox_acer)))
    def get_checkbox_asus(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.checkbox_asus)))
    def get_checkbox_msi(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.checkbox_msi)))

    def get_button_back(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.button_back)))

    def get_screen_size_16(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.screen_size_16)))
    def get_screen_size_17(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.screen_size_17)))

    def get_button_video_memory6gb(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_video_memory6gb)))

    def get_button_show_results(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_show_results)))

    def get_sort_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_button)))

    # если ошибка, элемент не кликабельный, то следует добавить "self.driver.execute_script("arguments[0].click();", low_price)"
    def get_low_price(self):
        low_price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.low_price)))
        self.driver.execute_script("arguments[0].click();", low_price)
        return low_price

    def get_scroll_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_add_to_cart(self):
        # если ElementClickInterceptedException, значит нужно прокрутить страницу, для этого строчка ниже
        self.driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))


    # Actions
    def click_filter_button(self):
        self.get_filter_button().click()
        print('Click Filter Button')

    def click_choice_minPrice(self):
        self.get_choice_minPrice().click()
        self.get_choice_minPrice().clear()
        self.get_choice_minPrice().send_keys('60000')
        print('Click Choice Min Price')

    def click_button_all(self):
        self.get_button_all().click()
        print('Click Button All')

    def click_checkbox_acer(self):
        self.get_checkbox_acer().click()
        print('Click Checkbox Acer')
    def click_checkbox_asus(self):
        self.get_checkbox_asus().click()
        print('Click Checkbox Asus')
    def click_checkbox_msi(self):
        self.get_checkbox_msi().click()
        print('Click Checkbox Msi')

    def click_button_back(self):
        self.get_button_back().click()
        print('Click Button Back')

    def click_screen_size_16(self):
        self.get_screen_size_16().click()
        print('Click Screen Size_16')
    def click_screen_size_17(self):
        self.get_screen_size_17().click()
        print('Click Screen Size_17')

    def click_button_video_memory6gb(self):
        self.get_button_video_memory6gb().click()
        print('Click Button Video Memory 6gb')

    def click_button_show_results(self):
        self.get_button_show_results().click()
        print('Click Button Show Results')

    def click_sort_button(self):
        self.get_sort_button().click()
        print('Click Sort Button')

    def click_low_price(self):
        self.get_low_price().click()
        print('Click Low Price')

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print('Click Add To Cart')


    # Methods
    def select_notebooks(self):
        self.get_current_url()
        self.assert_url("https://www.citilink.ru/catalog/noutbuki/")
        self.click_filter_button()
        self.slider_price(self.get_filter_price())
        self.click_choice_minPrice()
        self.click_button_all()
        self.click_checkbox_acer()
        time.sleep(3)
        self.click_checkbox_asus()
        time.sleep(3)
        self.click_checkbox_msi()
        time.sleep(3)
        self.click_button_back()
        self.click_screen_size_16()
        time.sleep(3)
        self.click_screen_size_17()
        time.sleep(3)
        self.click_button_video_memory6gb()
        time.sleep(3)
        self.click_button_show_results()
        time.sleep(3)
        self.click_sort_button()
        time.sleep(3)
        self.click_low_price()
        self.assert_text(self.get_catalog_price(), '126 510')
        self.scroll_to(self.get_scroll_to_cart())
        self.click_add_to_cart()
        time.sleep(3)
