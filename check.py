# Importing the webdriver from selenium package
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
service = Service('C:/Users/Aloukik/Downloads/edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get('https://www.google.com')
# Use find_element_by_xpath instead
text_area = driver.find_element(By.NAME, 'q')
text_area.send_keys('Sensex Today')

# search_field = driver.find_element(By.NAME, 'btnK')
# text_area.submit()

# Press the Enter key
text_area.send_keys(Keys.RETURN)
# Wait for 20 seconds
time.sleep(20)
# Close the browser
driver.quit()