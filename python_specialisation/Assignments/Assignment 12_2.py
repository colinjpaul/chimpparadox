import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')

total = 0
count = 0

print tags

for tag in tags:
    num = int(tag.contents[0])
    total += num
    count += 1

print ("Count", count)
print ("Sum", total)


