from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver = r"C:\Selenium\chromedriver.exe"
service_obj = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service_obj, options=options)
browser.get('https://selenium.dev/')
browser.maximize_window()

title = browser.title
print('Title is :', title)
