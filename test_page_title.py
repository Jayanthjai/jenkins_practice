from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
title=driver.title
assert title=='Automation Testing Practice'
