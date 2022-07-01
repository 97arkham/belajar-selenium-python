from lib2to3.pgen2 import driver
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/login")
# driver.find_element_by_id("username").send_keys("uno")
#click button by link
# driver.find_element_by_partial_link_text("Elemental Selenium").click()
#session atau jumlah link atau lain lain menggiunakan name
# link = driver.find_elements_by_name("a")
# print(len(link))

# menggunakan css selector
time.sleep(2)
# driver.find_element_by_css_selector("button.radius").click()
driver.find_element_by_css_selector("#login > button").click()