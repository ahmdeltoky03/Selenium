from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from time import sleep

chrome_driver = r"C:\selenium\chromedriver.exe"
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
url = "https://www.google.com"
driver.get(url)
sleep(5)
