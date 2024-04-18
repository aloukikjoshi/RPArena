from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Set the path to the EdgeDriver executable
service = Service('C:/Users/Aloukik/Downloads/edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get('https://www.google.com')
driver.quit()