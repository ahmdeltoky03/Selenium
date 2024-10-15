from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# chromedriver path in your pc
chrome_driver = r"C:\selenium\chromedriver.exe"
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

url = "https://demo.automationtesting.in/Resizable.html"
browser.get(url)
browser.maximize_window()

resizable_element = browser.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
intial_element_size = browser.find_element(By.XPATH,"//div[@id='resizable']")
intial_size = intial_element_size.size

print(f"Intial Element Size: {intial_size}")

time.sleep(2)
actions = ActionChains(browser)
actions.click_and_hold(resizable_element).move_by_offset(270, 152).release().perform()
time.sleep(2)
browser.quit()
