import re

line = 'From stephen.marguard@uct.ac.za Sat Jan   5  09:14:16 2008'
y = re.findall('@([^ ]*)', line)
print(y)

y = re.findall('^From .*@([^ ]*)', line)
print(y)

y = re.findall('@(\S*)', line)
print(y)

y = re.findall('From .*@(\S*)', line)
print(y)

line = 'X-DSPAM-Confidence: 0.8475'
y = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
print(y, len(y))