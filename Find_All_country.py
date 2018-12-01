import requests
from bs4 import BeautifulSoup
import re

pages = []

for i in range(0, 26):
    url = 'http://example.webscraping.com/places/default/index/' + str(i)
    pages.append(url)


for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    titles = soup.findAll('a', href=re.compile('view'))

    for title in titles:
        print(title.text)
