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

url = "https://the-internet.herokuapp.com/broken_images"
browser.get(url)
browser.maximize_window()

all_images = browser.find_elements(By.TAG_NAME, "img")

broken_image = []
for image in all_images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_image.append(src)
            print("Broken Image Found")

if broken_image:
    for image in broken_image:
        print(image)
browser.close()
