from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Configura el controlador del navegador
edge_options = Options()
edge_options.use_chromium = True  # Utiliza el motor Chromium de Edge


edge_service = Service(executable_path='msedgedriver.exe')
driver = webdriver.Edge(service=edge_service, options=edge_options)

stock_sym = "LLY"
period1 = "1536624000"
period2 = "1694390400"
#https://finance.yahoo.com/quote/LLY/history?period1=1536624000&period2=1694390400
# Abre la página web
driver.get("https://finance.yahoo.com/quote/"+stock_sym+"/history?period1="+period1+"&period2="+period2)

# Haz scroll para cargar más datos (puedes repetir esto según sea necesario)
# Seleccionamos un elemento de la página web
body = driver.find_element(By.TAG_NAME, 'body')
pos_ini = driver.execute_script("return window.scrollY;")

while True:
    body.send_keys(Keys.END);
    time.sleep(0.6)
    pos_new = driver.execute_script("return window.scrollY;")
    if pos_ini == pos_new: break
    else: pos_ini = pos_new

# Espera un tiempo para que se carguen los datos (ajusta según tu caso)
time.sleep(2)

# Extrae el HTML después de haber cargado más datos

LLY_html = driver.page_source

# Cierra el navegador
driver.quit()