import urllib
import json

location = raw_input('Enter location: ')

# hardcode location for testing
# location = "http://python-data.dr-chuck.net/comments_271857.json"

count = 0
total = 0

print 'Retrieving', location

uh = urllib.urlopen(location)
data = uh.read()

print 'Retrieved ', len(data), 'characters'

info = json.loads(data)
comments = info['comments']

comment_count = 0
total = 0

for item in comments:
    name = item['name']
    count = item['count']
    comment_count += 1
    total += count

print 'Count', comment_count
print 'Total', total



