from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demoqa.com/login")
driver.get("https://demoqa.com/books")
driver.find_element_by_id("login").click()