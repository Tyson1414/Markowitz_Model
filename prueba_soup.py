from bs4 import BeautifulSoup
import prueba_selenium

soup = BeautifulSoup(prueba_selenium.LLY_html, 'html.parser')

table = soup.table

rows = table.find_all('tr')

matriz = []

for row in rows[1:]:
    datos = [td.text.strip() for td in row.find_all('td')]
    matriz.append(datos)
    #key = row.find_all('td')[1].text.strip()
    #value = row.find_all('td')[2].text.strip()
i = 0
for fila in matriz:
    print(i,fila[0])
    i += 1