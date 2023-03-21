import urllib.request, urllib.response
from bs4 import BeautifulSoup

url = input('Enter - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1745053.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
sum = 0
count = 0
for tag in tags:
    sum += int(tag.contents[0])
    count += 1

print('Count', str(count))
print('Sum', str(sum))
