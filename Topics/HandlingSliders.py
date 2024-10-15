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

url = "https://the-internet.herokuapp.com/horizontal_slider"
browser.get(url)
browser.maximize_window()


slider = browser.find_element(By.XPATH,"//input[@value='0']")
actions = ActionChains(browser)
actions.click_and_hold(slider).move_by_offset(50,0).release().perform()
time.sleep(5)
browser.quit()