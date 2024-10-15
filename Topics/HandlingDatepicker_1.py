from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import datetime,time
import requests

# chromedriver path in your pc
chrome_driver = r"C:\selenium\chromedriver.exe"
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

url = "https://www.globalsqa.com/demo-site/datepicker/"
browser.get(url)
browser.maximize_window()

browser.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()

frame = browser.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")
browser.switch_to.frame(frame)

browser.find_element(By.CSS_SELECTOR,"#datepicker").click()


formated_date = datetime.datetime.now().strftime("%m/%d/%y")
browser.find_element(By.CSS_SELECTOR,"#datepicker").send_keys(formated_date, Keys.ENTER)
time.sleep(5)
browser.close()