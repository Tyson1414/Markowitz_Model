from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Configura el controlador del navegador
edge_options = Options()
edge_options.use_chromium = True  # Utiliza el motor Chromium de Edge


edge_service = Service(executable_path='msedgedriver.exe')
driver = webdriver.Edge(service=edge_service, options=edge_options)

driver.get("https://stockanalysis.com/list/nyse-stocks/")

time.sleep(3)
button = driver.find_element(By.XPATH, "//button[contains(@class, 'controls-btn') and .//span[text()='500 Rows']]")
button.click()
time.sleep(3)
button = driver.find_element(By.XPATH, "//button[contains(@title, 'Show 1000 Rows')]")
button.click()
time.sleep(3)

page1 = driver.page_source

button = driver.find_element(By.XPATH, \
"//button[contains(@class, 'controls-btn xs:pl-1 xs:pr-1.5 bp:text-sm sm:pl-3 sm:pr-1') \
    and .//span[text()='Next']]")
button.click()
time.sleep(3)
page2 = driver.page_source

button.click()
time.sleep(3)
page3 = driver.page_source

driver.quit()