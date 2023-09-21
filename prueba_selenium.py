from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import sqlite3
import time

# Valores de marca de tiempo Unix
five_years = 157776400
fecha_actual_unix = int(time.time())

# Configura el controlador del navegador
edge_options = Options()
edge_options.use_chromium = True  # Utiliza el motor Chromium de Edge
edge_service = Service(executable_path='msedgedriver.exe')

#Algunas variables
period1 = str(fecha_actual_unix - five_years)
period2 = str(fecha_actual_unix)
control = True #variable de control

#ALGORITMO PARA SCRAPEAR LOS PRECIOS DE +2K STOCKS EN LOS ULTIMOS 5 AÑOS Y GUARDARLOS EN UNA BASE DE DATOS

#Obtenemos la cantidad de filas que tiene nuestra tabla stock

conn = sqlite3.connect('stocks.sqlite')
cur = conn.cursor()
cur.execute('SELECT COUNT(*) FROM Stock')
num_stocks = cur.fetchone()[0]

# Iteramos por cada una de la stocks
for stock in range(1 , num_stocks):
    #Obtenemos el Symbol de nuestra base de datos
    cur.execute('SELECT Symbol FROM Stock WHERE id = ?',(stock,))
    symbol = cur.fetchone()[0]
    print("https://finance.yahoo.com/quote/"+symbol+"/history?period1="+period1+"&period2="+period2)
    driver = webdriver.Edge(service=edge_service, options=edge_options)
    driver.get("https://finance.yahoo.com/quote/"+symbol+"/history?period1="+period1+"&period2="+period2)

    #Obtenemos la pagina html con la tabla de datos historicos
    body = driver.find_element(By.TAG_NAME, 'body')
    pos_ini = driver.execute_script("return window.scrollY;")
    while True:
        body.send_keys(Keys.END);
        time.sleep(0.6)
        pos_new = driver.execute_script("return window.scrollY;")
        if pos_ini == pos_new: break
        else: pos_ini = pos_new
    time.sleep(2)
    stock_html = driver.page_source
    driver.quit()

    #Extraemos la información de la pagina html
    soup = BeautifulSoup(stock_html, 'html.parser')
    table = soup.table
    if table is None: continue
    rows = table.find_all('tr')
    
    for row in rows[1:]:
        if len(row) < 7: continue
        date = row.find_all('td')[0].text.strip()
        price = row.find_all('td')[5].text.strip()
        cur.execute('INSERT OR IGNORE INTO Date (date) VALUES (?)', (date,))
        cur.execute('SELECT id FROM Date WHERE date = ? ', (date, ))
        date_id = cur.fetchone()[0]
        cur.execute('SELECT id FROM Stock WHERE symbol = ? ', (symbol, ))
        symbol_id = cur.fetchone()[0]
        cur.execute('''INSERT OR IGNORE INTO Historical (price,date_id,stock_id) VALUES (?,?,?)''',
                    (price,date_id,symbol_id,))
    conn.commit()



