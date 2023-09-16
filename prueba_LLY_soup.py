from bs4 import BeautifulSoup
import prueba_selenium
import sqlite3

soup = BeautifulSoup(prueba_selenium.LLY_html, 'html.parser')

table = soup.table

rows = table.find_all('tr')
matriz = []

for row in rows[1:]:
    if len(row) < 7: continue
    columna1 = row.find_all('td')[0].text.strip()
    columna2 = row.find_all('td')[5].text.strip()
    datos = [columna1, columna2]
    matriz.append(datos)


conn = sqlite3.connect('stocks.sqlite')
cur = conn.cursor()
for row in matriz:
    cur.execute('INSERT OR IGNORE INTO Date (date) VALUES (?)', (row[0],))
    cur.execute('SELECT id FROM Date WHERE date = ? ', (row[0], ))
    date_id = cur.fetchone()[0]
    cur.execute('SELECT id FROM Stock WHERE symbol = ? ', (prueba_selenium.stock_sym, ))
    symbol_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Historical 
    (price,date_id,stock_id) VALUES (?,?,?)''', 
    (row[1],date_id,symbol_id,))

conn.commit()