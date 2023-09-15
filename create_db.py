import stock_soup
import stock_selenium
import sqlite3

def table_names(dic):
    for key,value in dic.items():
        cur.execute('INSERT OR IGNORE INTO Stock (Symbol, Name) VALUES (?, ?)', (key, value,))

conn = sqlite3.connect('stocks.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Stock;

CREATE TABLE IF NOT EXISTS Stock
    (id INTEGER PRIMARY KEY, Symbol TEXT UNIQUE, Name TEXT);

CREATE TABLE IF NOT EXISTS Date
    (id INTEGER PRIMARY KEY, date TEXT);

CREATE TABLE IF NOT EXISTS Historical
    (id INTEGER PRIMARY KEY, stock_id INTEGER, date_id INTEGER, price FLOAT);

''')
        
table_names(stock_soup.extract_table(stock_selenium.page1))
table_names(stock_soup.extract_table(stock_selenium.page2))
table_names(stock_soup.extract_table(stock_selenium.page3))

conn.commit()