from selenium import webdriver
from selenium.webdriver.common.by import By

def test_1_single_input_field():

    driver = webdriver.Chrome()

    # Go to testing site
    driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

    # Enter message
    my_message = 'My testing message'
    driver.find_element(By.ID, 'user-message').send_keys(my_message)

    # Show message
    form_one = driver.find_element(By.ID, 'get-input')
    form_one.find_element(By.CLASS_NAME, 'btn').click()
    displayed_message = driver.find_element(By.ID, 'display').text

    assert displayed_message == my_message

def test_2_two_input_fields():

    driver = webdriver.Chrome()
    a = 5
    b = 10
    # Go to testing site
    driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

    # Enter a
    driver.find_element(By.ID, 'sum1').send_keys(a)

    # Enter b
    driver.find_element(By.ID, 'sum2').send_keys(b)


    # Show message
    form_two = driver.find_element(By.ID, 'gettotal')
    form_two.find_element(By.CLASS_NAME, 'btn').click()
    displayed_total = driver.find_element(By.ID, 'displayvalue').text

    assert displayed_total == str(a+b)
