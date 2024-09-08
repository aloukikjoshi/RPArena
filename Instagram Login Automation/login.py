import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')

driver = webdriver.Edge()
driver.get('https://www.instagram.com')

# Wait for the username field to be present
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'username'))
)
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'password'))
)

username_field.send_keys(username)
password_field.send_keys(password)
# Press the Enter key
password_field.send_keys(Keys.RETURN)

# Wait for the user to log in
time.sleep(60)

# Periodically check if the user has logged out
while True:
    try:
        # Check for the presence of the login elements
        driver.find_element(By.NAME, 'username')
        driver.find_element(By.NAME, 'password')
        print("User has logged out. Closing the driver.")
        break
    except:
        # If login elements are not found, continue checking
        time.sleep(5)

# Close the browser
driver.quit()