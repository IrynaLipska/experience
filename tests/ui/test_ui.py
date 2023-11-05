import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_incorrect_username():
    #controlling object
    #driver = webdriver.Chrome(
    #    service=Service(r'C:\\Users\\user\\experience' + 'chromedriver.exe')
    #)
    #creating an object 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    #opening page
    driver.get("https://github.com/login")

    #finding log field
    login_elem = driver.find_element(By.ID, "login_field")

    #enter wrong data
    login_elem.send_keys("i_lipska@mistakeinemail.com")
    #time.sleep(3)
                         
    #finding password field
    pass_elem = driver.find_element(By.ID, "password")

    #enter wrong password
    pass_elem.send_keys("wrong password")
    #time.sleep(3)

    #finding button sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    #leftClick
    btn_elem.click()
    #time.sleep(3)

    #check page
    assert driver.title == "Sign in to GitHub · GitHub"
    #time.sleep(3)

    #closing browser
    driver.close()

    