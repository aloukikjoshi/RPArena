from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import pandas as pd

excel_file_path = "C:/Users/Aloukik/Desktop/bookstore.xlsx"

service = Service("C:/Users/Aloukik/Downloads/edgedriver_win64 (1)/msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.get("https://automationbookstore.dev/")
data_element = driver.find_elements(By.XPATH, "//*[@id='productList']/li")
data = []
for element in data_element:
    data.append(element.text)

df = pd.DataFrame(data, columns=['Books'])
df.to_excel(excel_file_path, index=True)
driver.quit()