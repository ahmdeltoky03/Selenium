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

url = "https://jqueryui.com/"
browser.get(url)
browser.maximize_window()

all_links = browser.find_elements(By.TAG_NAME, "a")
print(f'Total Number of links: {len(all_links)}')
for link in all_links:
    href = link.get_attribute("href")
    response = requests.get(href)
    if response.status_code >= 400:
        print(f'Broken Link Found: {href}. status code : {response.status_code}')

browser.quit()