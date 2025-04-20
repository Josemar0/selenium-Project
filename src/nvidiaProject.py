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

buttons = driver.find_elements(By.CLASS_NAME,"nv-teaser-button")

series = input("Which Graphic Card Series? ")

print("searching...")
for button in buttons:
    link = button.get_attribute("href")
    if link and series in link:
        WebDriverWait(driver,5).until(
            EC.element_to_be_clickable(button)
        )
        button.click()
        break

buttons = driver.find_elements(By.CLASS_NAME,"btncta")

print("finding prices...")
for button in buttons:
    link = button.get_attribute("href")
    if link and "#shop" in link:
        WebDriverWait(driver,5).until(
            EC.element_to_be_clickable(button)
        )
        button.click()
        break

card_names = driver.find_elements(By.XPATH,"//h3[contains(text(),'GeForce RTX')]")
starting_prices = driver.find_elements(By.XPATH,"//div[contains(text(),'Starting at $')")

print("Card Names: ")
for name in card_names:
    print(name.text)

for price in starting_prices:
    print("Price: ")
    print(price.text)
time.sleep(5)

driver.quit()

