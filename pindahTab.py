from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="content"]/div/a').click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])

