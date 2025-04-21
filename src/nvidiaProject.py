from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with

import time

driver = webdriver.Chrome()
driver.set_window_size(1024,1024)
driver.get("https://www.nvidia.com/en-us/geforce/graphics-cards/")

cookies = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler"))
 )
driver.execute_script("arguments[0].click();", cookies)

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

print("finding cards...")
for button in buttons:
    link = button.get_attribute("href")
    if link and "#shop" in link:
        WebDriverWait(driver,5).until(
            EC.element_to_be_clickable(button)
        )
        button.click()
        break

card_names = driver.find_elements(By.XPATH,"//h3[contains(text(),'GeForce RTX')]")

for name in card_names:
    print(name.text)
    if(series == "40"):
        print("unavailable")
if(series != "40"):
    card_name = input("Select Card: ")

    card = None

    for name in card_names:
        if name.text and card_name in name.text:
            card = name

    button = driver.find_element(locate_with(By.CLASS_NAME,"btn-text").below(card))

    ActionChains(driver).scroll_to_element(button).perform()

    WebDriverWait(driver,5).until(EC.element_to_be_clickable(button)).click()

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"fa-xmark"))).click()


time.sleep(15)

driver.quit()

