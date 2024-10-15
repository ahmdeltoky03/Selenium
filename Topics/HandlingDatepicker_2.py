from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import datetime, time
import requests

# chromedriver path in your pc
chrome_driver = r"C:\selenium\chromedriver.exe"
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)
browser.maximize_window()

# time.sleep(5)
browser.find_element(By.ID, 'datepicker2').click()
time.sleep(5)

current_month = datetime.datetime.now().month
current_year = datetime.datetime.now().year

next_day = datetime.datetime.now() + datetime.timedelta(days=1)
Next_day = str(next_day.day)
next_months = (current_month % 12) + 1

next_months_year = f"{next_months}/{current_year}"
# print(type(next_months_year))

month_Dropdown = browser.find_element(By.CSS_SELECTOR, "select[title='Change the month']")
select = Select(month_Dropdown)
select.select_by_value(str(next_months_year))

year_dropdown = browser.find_element(By.CSS_SELECTOR,"select[title='Change the year']")
select = Select(year_dropdown)
select.select_by_visible_text("2020")

browser.find_element(By.LINK_TEXT,Next_day).click()
print(Next_day)
print(next_months_year)
print(current_year)
time.sleep(5)
browser.close()