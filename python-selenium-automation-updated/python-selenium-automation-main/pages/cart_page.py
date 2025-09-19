from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    # TOTAL_TXT = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    ITEM_COUNT = (By.CSS_SELECTOR, '[class=styles_summary-subheading__Dg400]')

    def open_cart(self):
        self.open_url('https://www.target.com/cart')

    def verify_cart_empty_msg(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_cart_items(self,amount):
        print(amount)
        expected_partial_text = f'{amount} item'
        self.verify_partial_text(expected_partial_text, *self.ITEM_COUNT)
