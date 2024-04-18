from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service('C:/Users/Aloukik/Downloads/edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get('https://codenboxautomationlab.com/registration-form/')

wait = WebDriverWait(driver, 10)

first_name = wait.until(EC.presence_of_element_located((By.NAME, 'fname')))
first_name.send_keys('Aloukik')
last_name = wait.until(EC.presence_of_element_located((By.NAME, 'lname')))
last_name.send_keys('Joshi')
email = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
email.send_keys('aloukikjoshi@gmail.com')
phone_no = wait.until(EC.presence_of_element_located((By.NAME, 'nf-field-20')))
phone_no.send_keys('9644388291')
course = Select(wait.until(EC.presence_of_element_located((By.NAME, 'nf-field-22'))))
course.select_by_visible_text('Selenium Automation')
month_of_batch = Select(wait.until(EC.presence_of_element_located((By.NAME, 'nf-field-24'))))
month_of_batch.select_by_visible_text('May')
others_radio_button = wait.until(EC.presence_of_element_located((By.ID, 'nf-label-class-field-23-6')))
others_radio_button.click()
register = wait.until(EC.presence_of_element_located((By.ID, 'nf-field-15')))
register.click()

time.sleep(20)
driver.quit()