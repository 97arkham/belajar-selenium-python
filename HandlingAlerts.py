from lib2to3.pgen2 import driver
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="alertButton"]').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="confirmButton"]').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="confirmButton"]').click()
time.sleep(2)
driver.switch_to.alert.dismiss()