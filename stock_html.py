from bs4 import BeautifulSoup
import urllib
import pandas as pd
import requests

# Scrape stock symbols from website
site_url = "https://stockanalysis.com/list/nyse-stocks/"
# Trampa para engañar el servidor
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
r = requests.get(site_url, headers=headers)
# El codigo de estado 200 nos indica que todo está 'OK'
if r.status_code == 200:
    site_content = r.text

with open('500_stocks.html', 'w', encoding='utf-8') as f:
    f.write(site_content)