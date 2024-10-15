from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import requests

# chromedriver path in your pc
chrome_driver = r"C:\selenium\chromedriver.exe"
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

browser.get('https://cosmocode.io/automation-practice-webtable/')
browser.maximize_window()

table = browser.find_element(By.ID, 'countries')
rows = table.find_elements(By.TAG_NAME, 'tr')
print(f'Number of rows: {len(rows)}')

taget_value = 'Algeria'
for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')

    for cell in cells:
        if taget_value in cell.text:
            print(f'Target Value is Found')
        # print(cell.text, end=" ")