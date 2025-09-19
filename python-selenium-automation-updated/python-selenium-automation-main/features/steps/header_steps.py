from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



# SEARCH_FIELD = (By.ID, 'search')
# SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
# CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
HEADER_LINKS = (By.CSS_SELECTOR, '[data-test*="web/GlobalHeader/UtilityHeader/"]')
TARGET_CIRCLE_HEADER = (By.CSS_SELECTOR, "[data-test='@web/Circle/PageTitle']")
TARGET_SIGN_IN_HEADER = (By.CSS_SELECTOR, "[class*='styles_ndsHeading']")

@when('Search for {search_word}')
def search_product(context, search_word):
    print(search_word)
    context.app.header.search_product(search_word)
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN).click()

@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()
    # context.driver.find_element(*CART_ICON).click()

@when('Click on 1st header link')
def click_1st_link(context):
    element = context.driver.find_element(*HEADER_LINKS)
    # print('Before refresh')
    # print(element)
    context.driver.refresh()
    # print('After refresh')
    element = context.driver.find_element(*HEADER_LINKS)
    # print(element)
    element.click()

@when('Click Sign In')
def click_sign_in(context):
    context.app.header.click_sign_in()
    # context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()

@when('From right side navigation menu, click Sign In')
def click_nav_sign_in(context):
    context.app.header.click_nav_sign_in()
    sleep(5)

@then('Verify header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links, found {len(links)}'

@then('Verify Target Circle opens')
def verify_header_link_count(context):
    context.driver.find_element(*TARGET_CIRCLE_HEADER)

@then('Verify Sign In form opened')
def verify_sign_in_opened(context):
    context.driver.find_element(*TARGET_CIRCLE_HEADER)

# @then('Verify header has links')
# def verify_header_link_count(context):
#     print(context.driver.find_elements(*HEADER_LINKS))
