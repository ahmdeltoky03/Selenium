from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# chromedriver path in your pc
chrome_driver = r"C:\selenium\chromedriver.exe"
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)
browser.maximize_window()

url = "https://www.google.com/"
browser.get(url)

viewports = [(1024, 768), (768, 1024), (768, 768), (1024, 1024)]

try:
    for viewport in viewports:
        browser.set_window_size(*viewport)
        sleep(2)
finally:
    browser.close()