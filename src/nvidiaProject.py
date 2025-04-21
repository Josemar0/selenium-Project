import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with

import time

driver = uc.Chrome()
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
    original_window = driver.current_window_handle

    button = driver.find_element(locate_with(By.CLASS_NAME,"btn-text").below(card))

    ActionChains(driver).scroll_to_element(button).perform()

    driver.delete_all_cookies()
# Clear local storage
    driver.execute_script("window.localStorage.clear();")
# Clear session storage
    driver.execute_script("window.sessionStorage.clear();")

    WebDriverWait(driver,5).until(EC.element_to_be_clickable(button)).click()

    WebDriverWait(driver,5).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    cookies = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler"))
    )
    driver.execute_script("arguments[0].click();", cookies)
    
    products = driver.find_elements(By.CLASS_NAME,"nv-productTitle")
    product_prices = driver.find_elements(By.CLASS_NAME,"decimal")
    for product in products:
        print(product.text)
        time.sleep(1)


    for price in product_prices:
        print(price.text)
        time.sleep(1)

time.sleep(15)

driver.quit()

