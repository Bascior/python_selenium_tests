from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
Uplod a file using input.
'''

page = 'http://the-internet.herokuapp.com/upload'
filepath = "C:/.../..."          # File path to your file on your local machine

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(15)
browser.get(page)

# Choose a file to upload
browser.find_element(By.ID, 'file-upload').send_keys(filepath)
# Submit the file
browser.find_element(By.ID, 'file-submit').click()

# Check if the file is uploaded by checking siet title and file name
result_title = browser.find_element(By.TAG_NAME, 'h3').text
print(result_title)
uploaded_file_name = browser.find_element(By.ID, 'uploaded-files').text
print('File:', uploaded_file_name)
