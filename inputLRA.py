from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get("https://fmis.bpkp.go.id/rembangkab")

driver.maximize_window()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="hero"]/div/div/div[1]/div/div/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="kduser"]').send_keys('')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('')
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
time.sleep(2)
driver.get("https://rembangkab.fmis.id/akuntansi/skpd/saldo-awal/lra-lak")


