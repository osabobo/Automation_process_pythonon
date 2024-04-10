from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

web = 'https://www.thesun.co.uk/sport/football/'
path = "C://chromedriver.exe"# introduce path here

# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)
# Finding Elements
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

for container in containers [:2]:
    title = container.find_element(by='xpath', value='./a/h3').text
    print(title)