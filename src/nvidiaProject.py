from selenium import webdriver;
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

#describes session,require for remote
option = webdriver.ChromeOptions()
option.timeouts = {'implicit': 5}
option.binary_location = "/usr/bin/chromium-browser"

#creates path to chromedriver
path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(path,"..","lib","chromedriver-linux64","chromedriver")

#manages starting and stopping of local drivers, not remote
services = Service(executable_path=path)

#what controls/launches the browser
driver = webdriver.Chrome(options=option, service=services)
driver.get("https://www.nvidia.com/en-us/geforce/graphics-cards/")

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sub-brand-item"))
 )
product_menu = driver.find_element(By.CLASS_NAME, "sub-brand-item")
product_menu.click()

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Graphics Cards & Desktops')]"))
)
product_type = driver.find_element(By.XPATH, "//div[contains(text(),'Graphics Cards & Desktops')]")

product_type.click()

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'RTX 5090')]"))
)
product_name = driver.find_element(By.XPATH, "//div[contains(text(),'RTX 5090')]")


time.sleep(5)

driver.quit()

