from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@given('Open Target cart Page')
def open_main(context):
    context.driver.get('https://www.target.com/cart')
    sleep(5)


@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart_msg(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

@then('Verify cart has correct product')
def verify_product_name(context):
    # context.product_name => stored before
    sleep(5)
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    print('Name in cart: ', product_name_in_cart)
    assert context.product_name[:5] == product_name_in_cart[:5], \
        f'Expected {context.product_name[:5]} did not match {product_name_in_cart[:5]}'