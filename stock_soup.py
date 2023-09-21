import stock_selenium
from bs4 import BeautifulSoup

def extract_table(page):

    soup = BeautifulSoup(page, 'html.parser')

    table = soup.table
    rows = table.find_all('tr')
    companies = {}
    for row in rows[1:]:
        key = row.find_all('td')[1].text.strip()
        value = row.find_all('td')[2].text.strip()
        companies[key] = value
    return companies