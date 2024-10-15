import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chromedriver path in your pc
chrome_driver = r"C:\selenium\chromedriver.exe"
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

url = "https://the-internet.herokuapp.com/dropdown"
browser.get(url)
browser.maximize_window()

dropdown_element = browser.find_element(By.ID, 'dropdown')
select = Select(dropdown_element)

# time.sleep(2)
# select.select_by_visible_text('Option 1')
# time.sleep(2)
# select.select_by_visible_text('Option 2')
# # time.sleep(2)
# # select.select_by_index(2)
target_option = "Option 2"
for option in select.options:
    # print(option.text)
    if option.text == target_option:
        select.select_by_visible_text(target_option)
        break
    else:
        print(f'{target_option} not selected')
