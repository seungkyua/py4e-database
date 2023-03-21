import urllib.request
from bs4 import BeautifulSoup
import re


def get_url(url, position):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    href = tags[position-1].get('href', None)
    name = re.findall('http://py4e-data.dr-chuck.net/known_by_(.+).html', href)
    names.append(name)
    return href


url = input('Enter URL: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
count = int(input('Enter count: '))
position = int(input('Enter position: '))

names = list()
name = re.findall('http://py4e-data.dr-chuck.net/known_by_(.+).html', url)
names.append(name)

for i in range(count):
    url = get_url(url, position)

print(names[-1])
