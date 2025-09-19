from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(5)

expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//h1[contains(@class,'Heading')]").text
assert expected_text in actual_text, f'error,text is not in {actual_text}'

driver.find_element(By.ID, 'login')

sleep(5)
