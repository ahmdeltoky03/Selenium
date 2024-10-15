# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
# import requests
#
# # chromedriver path in your pc
# chrome_driver = r"C:\selenium\chromedriver.exe"
# service = Service(chrome_driver)
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(service=service, options=options)
#
# url = "https://the-internet.herokuapp.com/iframe"
# browser.get(url)
# browser.maximize_window()
#
# iframe = browser.find_element(By.ID, "mce_0_ifr")
# browser.switch_to.frame(iframe)
#
# text_editor = browser.find_element(By.ID, "tinymce")
# text_editor.clear()
# text_editor.send_keys("Iframe Iframe")
# # time.sleep(5)
#
# browser.switch_to.default_content()
# selenium_link = browser.find_element(By.XPATH, "//a[normalize-space()='Elemental Selenium']")
# selenium_link.click()
