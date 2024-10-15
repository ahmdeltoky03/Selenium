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
driver = webdriver.Chrome(service=service, options=options)

url = "https://tdb.tanta.edu.eg/newemailservices/pw_reset.aspx"
driver.get(url)
driver.maximize_window()

ssn = "30308281600655"
select_collage = driver.find_element(By.CSS_SELECTOR, "#DropDownList1")
select_collage.click()
select = Select(select_collage)
select.select_by_value("2")

driver.find_element(By.ID, "TextBox1").send_keys(ssn)