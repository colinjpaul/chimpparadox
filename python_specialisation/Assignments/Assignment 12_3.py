import urllib
from BeautifulSoup import *

#  Course requires you use file copied to local directory
#  For all other purposes 'import bs4'

#url = raw_input('Enter URL: ')
url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'

currentCount = 0
count = raw_input("Enter count: ")
count = int(count)

position = raw_input("Enter position: ")
position = int(position)

print('Retrieving: ' + url)

while currentCount < count:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    tag = tags[position]
    url = tag.get('href', None)
    print ('Retrieving: ' + url)
    currentCount += 1




'''
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
tag = tags[position]

url = tag.get('href', None)
print (url)


html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
tag = tags[position]

url = tag.get('href', None)
print (url)


html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
tag = tags[position]

url = tag.get('href', None)
print (url)









def crawl(followme):
    html = urllib.urlopen(followme).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))

#url = raw_input('Enter URL: ')


#count = raw_input("Enter count: ")
position = raw_input("Enter position: ")

#currentCount = 0
currentPosition = 1

if currentPosition == int(position):

crawl(url)

while currentCount < count:
    if currentPosition == int(position):
        print("Retrieving: " + url)
        crawl(url)
    currentPosition += 1
currentCount += 1

print("Retrieving: " + url)

while currentCount < 4:
    for tag in tags:
        if currentPosition == int(position):
            followMe = tag.get('href', None)
            print("Retrieving: " + followMe)
            html = urllib.urlopen(followMe).read()
            soup = BeautifulSoup(html)
            tags = soup('a')

    if position == 3:
        print tag.contents[0]

    num = int(tag.contents[0])
'''
