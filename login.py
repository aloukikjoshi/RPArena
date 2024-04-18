# Importing the webdriver from selenium package
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
service = Service('C:/Users/Aloukik/Downloads/edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get('https://www.instagram.com')
username_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')
username_field.send_keys("aloukikjoshi")
password_field.send_keys("Aloukik")
# Press the Enter key
password_field.send_keys(Keys.RETURN)

time.sleep(150)
# Close the browser
driver.quit()