from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_progress_bar():

    driver = webdriver.Chrome()

    # Go to testing site
    driver.get('https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html')

    percentage_value = driver.find_element(By.CLASS_NAME, 'percenttext').text
    # Check if the percentage value i equal 0 at the beginning
    assert str(percentage_value) == '0%'

    # Click download button
    driver.find_element(By.ID, 'cricle-btn').click()
    # Wait until download process is finish by checking percentage value, if it is equal 100% test is passed
        #TO DO

