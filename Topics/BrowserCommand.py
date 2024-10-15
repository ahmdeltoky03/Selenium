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

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
browser.get(url)
sleep(5)
browser.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
sleep(5)
browser.back()
sleep(5)
browser.refresh()
sleep(5)
browser.forward()
sleep(5)
browser.quit()
