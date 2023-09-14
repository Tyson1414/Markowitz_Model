import stocks_soup
import stock_selenium
import sqlite3


conn = sqlite3.connect('stocks.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS names')
cur.execute('''CREATE TABLE IF NOT EXISTS names
    (id INTEGER PRIMARY KEY, symbol TEXT UNIQUE, name TEXT)''')

def table_names(dic):
    for key,value in dic.items():
        cur.execute('INSERT OR IGNORE INTO names (symbol, name) VALUES (?, ?)', (key, value,))
        conn.commit()

table_names(stocks_soup.extract_table(stock_selenium.page1))
table_names(stocks_soup.extract_table(stock_selenium.page2))
table_names(stocks_soup.extract_table(stock_selenium.page3))