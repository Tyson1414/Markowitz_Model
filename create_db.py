import stock_soup
import sqlite3


conn = sqlite3.connect('stocks.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS names
    (id INTEGER PRIMARY KEY, symbol TEXT UNIQUE, name TEXT)''')

for key,value in stock_soup.companies.items():
    #print(f'Clave: {key}, Valor: {value}')
    cur.execute('INSERT OR IGNORE INTO names (symbol, name) VALUES (?, ?)', (key, value,))
conn.commit()