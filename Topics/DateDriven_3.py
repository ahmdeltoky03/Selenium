# Data Driven Testing using JSON
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import json
from time import sleep


chrome_driver = r"C:\selenium\chromedriver.exe"
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
url = "https://www.saucedemo.com/"

json_file = 'test_Data.json'
with open(json_file,'r') as f:
    data = json.load(f)

for row in data['users']:
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    driver.find_element(By.ID, 'user-name').send_keys(row['username'])
    driver.find_element(By.ID, 'password').send_keys(row['password'])
    driver.find_element(By.ID, "login-button").click()
    sleep(2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Open Menu']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
    sleep(2)

driver.close()
