from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
for i in range(3):
    driver.get("https://www.malasngoding.com/")

    try:
        WebDriverWait(driver,30).until(EC.visibility_of_all_elements_located((By.XPATH,'/html/body/div[4]')))
        print("muncul")
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/button/span').click()
        print("sukses close")

    except TimeoutException:
        print("gak muncul")
        pass

    time.sleep(3)