from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from openpyxl import load_workbook
import time

wb = load_workbook(filename="D:\koding\selenium\SELNIUMCB.xlsx")

sheetRange = wb['Sheet1']

driver = webdriver.Chrome()

driver.get('https://demoqa.com/webtables')
driver.maximize_window()
driver.implicitly_wait(20)

# looping input

i = 2

while i <=len(sheetRange['A']):
    Firstname = sheetRange['A'+str(i)].value
    lastname = sheetRange['B'+str(i)].value
    email = sheetRange['C'+str(i)].value
    age = sheetRange['D'+str(i)].value
    salary = sheetRange['E'+str(i)].value
    departemen = sheetRange['F'+str(i)].value

    driver.find_element_by_xpath('//*[@id="addNewRecordButton"]').click()

    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div')))

        driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(Firstname)
        driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(lastname)
        driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys(email)
        driver.find_element_by_xpath('//*[@id="age"]').send_keys(age)
        driver.find_element_by_xpath('//*[@id="salary"]').send_keys(salary)
        driver.find_element_by_xpath('//*[@id="department"]').send_keys(departemen)
        driver.find_element_by_xpath('//*[@id="submit"]').click()

    except TimeoutException:
        print("gak muncul cuy")
        pass

    time.sleep(1)
    i += 1
print("selesai")