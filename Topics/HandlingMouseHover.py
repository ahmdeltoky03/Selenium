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
browser.maximize_window()

url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

actions = ActionChains(browser)
hover_element = browser.find_element(By.XPATH, "//a[normalize-space()='Widgets']")
actions.move_to_element(hover_element).perform()
# browser.find_element(By.XPATH, "//a[normalize-space()='Widgets']")
