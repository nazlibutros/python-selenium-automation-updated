from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



# SEARCH_FIELD = (By.ID, 'search')
# SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
# CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
HEADER_LINKS = (By.CSS_SELECTOR, '[data-test*="web/GlobalHeader/UtilityHeader/"]')

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

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()

@then('Verify header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links, found {len(links)}'

# @then('Verify header has links')
# def verify_header_link_count(context):
#     print(context.driver.find_elements(*HEADER_LINKS))
