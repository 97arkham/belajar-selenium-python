from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

driver.maximize_window()