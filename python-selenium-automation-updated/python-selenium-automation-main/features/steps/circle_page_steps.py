from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_CELLS = (By.CSS_SELECTOR, '[class="cell-item-content"]')

@given('Open Target circle Page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify there are at least 10 benefit cells')
def verify_header_link_count(context):
    benefit_cells = context.driver.find_elements(*BENEFIT_CELLS)
    print(len(benefit_cells))
    assert len(benefit_cells) >= 10, f'Expected at least 10 benefits, found {len(benefit_cells)}'
