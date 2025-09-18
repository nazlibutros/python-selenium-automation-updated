from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
# CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
TOTAL_TXT = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")

@when('Open Target cart Page')
def open_main(context):
    context.driver.get('https://www.target.com/cart')

@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart_msg(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*TOTAL_TXT).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"

@then('Verify cart has correct product')
def verify_product_name(context):
    # context.product_name => stored before
    product_name_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    print('Name in cart: ', product_name_in_cart)

    assert context.product_name[:20] == product_name_in_cart[:20], \
        f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'