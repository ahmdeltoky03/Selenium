from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver = r"C:\selenium\chromedriver.exe"
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.ID, 'user-name').send_keys("standard_user")
driver.find_element(By.ID, 'password').send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Open Menu']").click()
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
element.click()
driver.close()
