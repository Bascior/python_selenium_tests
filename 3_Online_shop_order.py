from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
Online shop order process.
By one random item:
- add an item to the basket
- go through cashout process
'''

page = 'http://the-internet.herokuapp.com/add_remove_elements/'

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(15)
browser.get(page)