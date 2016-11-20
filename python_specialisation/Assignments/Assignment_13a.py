import urllib
import xml.etree.ElementTree as ET

location = raw_input('Enter location: ')

count = 0
total = 0

print 'Retrieving', location
uh = urllib.urlopen(location)
data = uh.read()
print 'Retrieved ', len(data), 'characters'

tree = ET.fromstring(data)

results = tree.findall('.//count')

for result in results:
    count += 1
    num = result.text
    num = int(num)
    total += num


print 'Count: ', count
print 'Sum: ', total







