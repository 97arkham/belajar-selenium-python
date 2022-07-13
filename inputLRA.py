from selenium import webdriver

import time
# import keyboard 

driver = webdriver.Chrome()

driver.get("")

driver.maximize_window()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="hero"]/div/div/div[1]/div/div/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="kduser"]').send_keys('')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('')
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
time.sleep(2)
driver.get("")

driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[5]/div/div/div[2]/div/div/div[1]/div[1]/a').click()

