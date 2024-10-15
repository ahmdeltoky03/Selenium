from selenium import webdriver
from selenium.webdriver import ActionChains
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

url = "https://the-internet.herokuapp.com/drag_and_drop"
browser.get(url)
browser.maximize_window()

source_element = browser.find_element(By.ID, "column-a")
destination_element = browser.find_element(By.ID, "column-b")

time.sleep(5)
actinos = ActionChains(browser)
actinos.drag_and_drop(source_element, destination_element).perform()
time.sleep(5)
browser.quit()
