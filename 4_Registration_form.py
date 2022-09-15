from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from random import randint
from selenium.webdriver.support.ui import Select

'''
Registration form. 
'''

page = 'https://www.way2automation.com/way2auto_jquery/registration.php#load_box'
# Variables:
name = 'Jan'
last_name = 'Nowak'
phone = '123123123'
username = 'User_1'
mail ='user@user.com'
filepath = 'C:/Users/.../...'       # Filepath to the picture which will be uploaded in the form
description = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
password = 'test_1'

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(15)
browser.get(page)

# Name and surname
browser.find_element(By.NAME, 'name').send_keys(name)
browser.find_element(By.XPATH, '//*[@id="register_form"]/fieldset[1]/p[2]/input').send_keys(last_name)

# Matrial status - random selection
browser.find_elements(By.NAME, 'm_status')[randint(0,2)].click()
# Hobby - random selection
browser.find_elements(By.NAME, 'hobby')[randint(0,2)].click()

# Country
country_dropdown = browser.find_element(By.XPATH, '/html/body/section/div[1]/div/div/form/fieldset[4]/select')
country_select = Select(country_dropdown)
country_select.select_by_value("India")

# Date of birth
# Month
birth_month_dropdown = browser.find_element(By.XPATH, '/html/body/section/div[1]/div/div/form/fieldset[5]/div[1]/select')
birth_month = Select(birth_month_dropdown)
birth_month.select_by_value('1')
# Day
day_month_dropdown = browser.find_element(By.XPATH, '/html/body/section/div[1]/div/div/form/fieldset[5]/div[2]/select')
day_month = Select(day_month_dropdown)
day_month.select_by_value('1')
# Year
year_month_dropdown = browser.find_element(By.XPATH, '/html/body/section/div[1]/div/div/form/fieldset[5]/div[3]/select')
year_month = Select(year_month_dropdown)
year_month.select_by_value('2014')

# Phone number
browser.find_element(By.NAME, 'phone').send_keys(phone)

# Username
browser.find_element(By.NAME, 'username').send_keys(username)

# E-mail
browser.find_element(By.NAME, 'email').send_keys(mail)

# Profile Picture
picture_section = browser.find_element(By.XPATH, '/html/body/section/div[1]/div/div/form/fieldset[9]')
picture_section.find_element(By.TAG_NAME, 'input').send_keys(filepath)

# About Yourself
browser.find_element(By.TAG_NAME, 'textarea').send_keys(description)

# Password
browser.find_element(By.NAME, 'password').send_keys(password)
# Confirm password
browser.find_element(By.NAME, 'c_password').send_keys(password)


