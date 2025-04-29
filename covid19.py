# modules
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# URL for scrapping data

url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

page_data = requests.get(url)

soup = BeautifulSoup(page_data.text, 'html.parser')

# print(soup)

data = []

# find all "td"
td_data = iter(soup.find_all ('td'))

print(td_data)

# data available in td_data

while True:
    try:
        country = next(td_data).text
        confirmed = next(td_data).text
        deaths = next(td_data).text
        continent = next(td_data).text

        data.append((country,
                     confirmed,
                     deaths,
                     continent))
        
    except StopIteration:
        break

print(data)

myTable = PrettyTable(["Country", "Cases", "Deaths", "Continent"])

for i in data:
    myTable.add_row(i)

print(myTable)
       
