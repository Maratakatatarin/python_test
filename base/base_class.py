import datetime
from selenium.webdriver import ActionChains


class Base():

    def __init__(self, driver):
        self.driver = driver


    """Method Get current url"""
    def get_current_url(self):
        # создаем переменную и сохраняем метод self.driver.current_url для того, чтобы выводить ее на печать в нашем терминале
        get_url = self.driver.current_url
        print('Current url ' + get_url)

    """Method assert url"""
    # передаем тот результат, который ожидаем
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')

    def slider_price(self, price):
        action = ActionChains(self.driver)
        #!!!!!!!!!ползунок двигается только в одно место, даже при "0"!!!!!!!!!!!
        action.click_and_hold(price).move_by_offset(0, 0).release().perform()
        # action.click_and_hold(price).move_by_offset(-50, 0).release().perform()
        print("Click Price")

    def scroll_to_sp(self, button):
        action = ActionChains(self.driver)
        action.move_to_element(button).perform()
        print("Scroll Page")

    def assert_price(self, price1, price2):
        assert price1 == price2
        print("The prices on the pages match")

    def assert_text(self, text_1, text_2):
        value_text_1 = text_1.text
        assert value_text_1 == text_2
        print("Locator: " + value_text_1 + ' = Text: ' + text_2)

        """Method Screenshot"""
    def get_screenshot(self):
        # today() - местное время без utc()
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        print(now_date)
        name_screenshot = 'screenshot' + now_date + ".png"
        # можно выставить задержку времени для загрузки страницы перед скриншотом
        self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\mVideo_project\\screen\\' + name_screenshot)


