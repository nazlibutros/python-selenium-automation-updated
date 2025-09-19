from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    NAV_SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def search_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(9)

    def click_cart(self):
        self.click(*self.CART_ICON)
        sleep(9)

    def click_sign_in(self):
        self.click(*self.SIGN_IN_BTN)
        sleep(9)

    def click_nav_sign_in(self):
        self.click(*self.NAV_SIGN_IN_BTN)
        sleep(9)


