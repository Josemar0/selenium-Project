from selenium import webdriver;
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def wait_and_click(element, wait_time=0) :
    time.sleep(wait_time)
    element.click

driver = webdriver.Chrome()

driver.get("https://www.nvidia.com/en-us/geforce/graphics-cards/")

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sub-brand-item"))
 )
product_menu = driver.find_element(By.CLASS_NAME, "sub-brand-item")

wait_and_click(product_menu)

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Graphics Cards & Desktops')]"))
)
product_type = driver.find_element(By.XPATH, "//div[contains(text(),'Graphics Cards & Desktops')]")

wait_and_click(product_type)

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'RTX 5090')]"))
)
product_name = driver.find_element(By.XPATH, "//div[contains(text(),'RTX 5090')]")

wait_and_click(product_name)

time.sleep(5)

driver.quit()

