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

url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)
browser.maximize_window()

# AlertButton = browser.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
AlertButton = browser.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']")
AlertButton.click()

alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(5)
alert.accept()
time.sleep(5)
browser.quit()

# time.sleep(5)
# alert.send_keys('Hi I am Alert')
# alert.accept()
# time.sleep(5)
# browser.quit()