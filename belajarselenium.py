from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/login")

