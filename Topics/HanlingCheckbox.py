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

url = "https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
browser.get(url)
browser.maximize_window()

# checkboxes = browser.find_elements(By.XPATH, '//input[@type="checkbox"]')
# for checkbox in checkboxes:
    # checkbox.send_keys(Keys.SPACE)
# days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

sleep(2)
browser.find_element(By.XPATH,"//label[normalize-space()='Sunday']").click()
sleep(2)
browser.find_element(By.XPATH,"//label[normalize-space()='Monday']").click()
sleep(2)
browser.find_element(By.XPATH,"//label[normalize-space()='Tuesday']").click()
sleep(2)
browser.find_element(By.XPATH,"//label[normalize-space()='Wednesday']").click()
sleep(2)
browser.find_element(By.XPATH,"//label[normalize-space()='Thursday']").click()
sleep(2)
browser.find_element(By.XPATH,"//label[normalize-space()='Friday']").click()
sleep(2)
browser.find_element(By.XPATH,"//label[normalize-space()='Saturday']").click()

sleep(2)
browser.close()
#
