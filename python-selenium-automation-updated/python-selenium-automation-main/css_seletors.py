from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Start Chrome browser:
driver = webdriver.Chrome()

driver.get('https://www.amazon.com/')

# CSS selector, using ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
# same as
driver.find_element(By.ID, 'twotabsearchtextbox')
# using class
driver.find_element(By.CSS_SELECTOR, '.icp-link-style-2')
driver.find_element(By.CSS_SELECTOR, '.icp-link-style-2.nav-a-2.nav-a')
# using ID and tag:
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')
# using ID and class
driver.find_element(By.CSS_SELECTOR, 'input.nav-progressive-attribute.nav-input')
# using ID and tag and class
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox.nav-progressive-attribute.nav-input')
# using attributes
driver.find_element(By.CSS_SELECTOR, '[aria-label="Search Amazon"]')
driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search Amazon"]')
# using tag + class + 2 attributes
driver.find_element(By.CSS_SELECTOR, 'input.nav-input[aria-label="Search Amazon"][role="searchbox"]')
# using partial match: taget signin header
driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsHeading']")
driver.find_element(By.CSS_SELECTOR, '[aria-controls*="results-container"][role="searchbox"]')

# ****HOMEWORK3****

# amazon logo
driver.find_element(By.CSS_SELECTOR, '[aria-label="Amazon"]')
# sign in or create account
driver.find_element(By.CSS_SELECTOR,'.a-size-medium-plus.a-spacing-small')
# textbox
driver.find_element(By.CSS_SELECTOR,'#claim-input-container')
# continue button
driver.find_element(By.CSS_SELECTOR,'.a-button-input')
# conditions of use
driver.find_element(By.CSS_SELECTOR,'[href*="signin_notification_condition_of_use"]')
# privacy notice
driver.find_element(By.CSS_SELECTOR,'[href*="signin_notification_privacy_notice"]')
# Need help
driver.find_element(By.CSS_SELECTOR,'.a-size-base.a-link-normal')
# create a free business account
driver.find_element(By.CSS_SELECTOR,'#ab-registration-ingress-link')