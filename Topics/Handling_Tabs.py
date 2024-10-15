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

browser.get('https://www.selenium.dev/')
browser.maximize_window()

time.sleep(2)
browser.switch_to.new_window()
browser.get('https://playwright.dev/')

print(f"Number of Tabs : {len(browser.window_handles)}")
tabs_value = browser.window_handles
print(tabs_value)
print(f"Current Window : {browser.current_window_handle}")

browser.find_element(By.CSS_SELECTOR,".getStarted_Sjon").click()

browser.switch_to.window(browser.window_handles[0])
browser.find_element(By.XPATH,"//span[normalize-space()='Downloads']").click()