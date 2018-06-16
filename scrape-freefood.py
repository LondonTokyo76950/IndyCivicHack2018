import csv
import requests
from bs4 import BeautifulSoup

url = 'http://www.freefood.org/zip.php?zip=10706'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
print(soup.body.div.div)
headings = soup.find_all("h2")
for heading in headings:
    print(heading.string)
    print(heading)
