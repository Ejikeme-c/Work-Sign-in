from selenium import webdriver
from datetime import datetime, timezone
from selenium.webdriver.common.by import By
import yaml


#importing the yml file that stores my password and username
with open('details.yml', 'r') as file: conf = yaml.safe_load(file)
my_email = conf['dentalcorp_user']['email']
my_password = conf['dentalcorp_user']['password']

driver = webdriver.Chrome()

def login(url, usernameId, username, passwordId, password, login_buttonId):
    driver.get(url)
    driver.find_element(By.ID, username).send_keys(username)
    driver.find_element(By.ID, passwordId).send_keys(password)
    driver.find_element(By.ID, login_buttonId).click()

def workday(url, workday_buttonId, launch_buttonId):
    driver.get(url)
    driver.find_element(By.CSS_SELECTOR, workday_buttonId).click()
    driver.find_element(By.CSS_SELECTOR, launch_buttonId).click()
  

def checkIn(checkIn_buttonId, ok_buttonId):
    driver.find_element(checkIn_buttonId).click()
    driver.find_element(ok_buttonId).click()

def checkOut(checkOut_buttonId, ok_buttonId):
    driver.find_element(checkOut_buttonId).click()
    driver.find_element(checkOut_buttonId).click() 




