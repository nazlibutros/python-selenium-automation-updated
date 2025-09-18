from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    sleep(10)
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Side navigation product did not appear'
    )
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN),
    #     message='Side navigation add to cart btn not clickable'
    # )

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored: ', context.product_name)

@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    # sleep(5)
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    # sleep(5)

@then('Verify search results are shown for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TXT).text
    assert product in actual_text, f'Error. Expected text {product} but got {actual_text}'