from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chromedriver path in your pc
chrome_driver = r"C:\selenium\chromedriver.exe"
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

browser.maximize_window()

# username, password
_username = "standard_user"
_password = "secret_sauce"

# url
login_url = "https://www.saucedemo.com/v1/"

browser.get(login_url)

# The place where it is written username, password
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")

# send username, password
username.send_keys(_username)
password.send_keys(_password)

# login place
login_button = browser.find_element(By.ID, "login-button")

# click button to login
login_button.click()

# Test
word = browser.find_element(By.CSS_SELECTOR, ".product_label")
assert word.text == "Products"
