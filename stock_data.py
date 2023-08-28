from bs4 import BeautifulSoup
import urllib
import pandas as pd
import requests

# Scrape stock symbols from website
site_url = "https://stockanalysis.com/list/nyse-stocks/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#r = urllib.request.urlopen(site_url)
r = requests.get(site_url, headers=headers)
#site_content = r.get(site_url, headers=headers)

if r.status_code == 200:
    site_content = r.text

with open('saved_page.html', 'w', encoding='utf-8') as f:
    f.write(site_content)