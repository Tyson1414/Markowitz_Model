import stock_html
from bs4 import BeautifulSoup

with open('500_stocks.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(),features="html.parser")

table = soup.table
#table_head = []
#table_head = table.thead.text
rows = table.find_all('tr')
companies = {}

for row in rows[1:]:
    key = row.find_all('td')[1].text.strip()
    value = row.find_all('td')[2].text.strip()
    companies[key] = value
