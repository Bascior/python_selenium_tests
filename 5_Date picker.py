from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

'''
** Date picker **

1. Send value to the input
2. Clear the input
3. Choose today on the bootstrap date picker
3. Clear the input
5. Choose a day on the bootstrap date picker

'''

page = 'https://demo.seleniumeasy.com/bootstrap-date-picker-demo.html'

# Variables
date_sample = '07.06.2022'

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(15)
browser.get(page)

# 1. Send value to the input
datepicker_input = browser.find_element(By.CLASS_NAME, 'form-control')
datepicker_input.send_keys(date_sample)
datepicker_input.send_keys(Keys.ENTER)

time.sleep(3)

# 2. CLear the input
datepicker_input.clear()

time.sleep(3)

# 3. Choose today on the bootstrap date picker
datepicker_input.click()
today_date = browser.find_element(By.CLASS_NAME, 'today')
today_date.click()

time.sleep(3)

# 4. CLear the input
datepicker_input.clear()

time.sleep(3)

# 5. Choose a day on the bootstrap date picker
datepicker_button = browser.find_element(By.CLASS_NAME, 'input-group-addon').click()
day = browser.find_elements(By.TAG_NAME, 'td')[0].click()       # Choose the first day on presented bootstap



