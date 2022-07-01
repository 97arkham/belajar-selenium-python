from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

time.sleep(2)
# driver.find_element_by_xpath('//*[@id="content"]/div/button').click()
driver.find_element(By.XPATH,'//*[@id="content"]/div/button').click()


