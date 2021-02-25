from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.guidedolomiti.com/en/rock-climbing-grades/').text

soup = BeautifulSoup(source, 'lxml')

container = soup.find(id='advgb-cols-03818f8e-42fd-4047-954a-cc4719d51e39')

table = container.find('table')

with open ('routes.txt', 'w') as f:
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            f.write(cell.text.ljust(42))
        f.write('\n')
