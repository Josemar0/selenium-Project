from selenium import webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os
import re

driver = webdriver.Chrome()
driver.get("https://www.nvidia.com/en-us/geforce/graphics-cards/")

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "cmp-teaser__title"))
 )
series_options = driver.find_elements(By.CLASS_NAME, "cmp-teaser__title")

for series in series_options:
    print(series.text)

buttons = driver.find_elements(By.TAG_NAME,"a")

series = input("Which Graphic Card Series? ")

print("searching...")
for button in buttons:
    link = button.get_attribute("href")
    if link and series in link:
        WebDriverWait(driver,5).until(
            EC.element_to_be_clickable(button)
        )
        print("clicking...")
        button.click()
        break

time.sleep(5)
driver.quit()

