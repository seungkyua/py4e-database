import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


address = input('Enter location: ')
if len(address) < 1:
    address = 'http://py4e-data.dr-chuck.net/comments_42.xml'

uh = urllib.request.urlopen(address)

print('Retrieving', address)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

sum = 0
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)

print('Count:', len(counts))
print('Sum:', sum)


