# Data Driven Testing using CSV
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import csv
from time import sleep

chrome_driver = r"C:\selenium\chromedriver.exe"
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
# url = "https://www.saucedemo.com/"

csv_file = 'test_data.csv'
test_data = []  # list of Dictionary

with open(csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        test_data.append(row)
    print(test_data)

for row in test_data:
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
