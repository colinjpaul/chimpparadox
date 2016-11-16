import urllib
from BeautifulSoup import *

#  Course requires you use file copied to local directory
#  For all other purposes 'import bs4'

#url = raw_input('Enter URL: ')

url = "http://python-data.dr-chuck.net/known_by_Fikret.html"

def crawl():
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print(tags)

crawl()

'''


count = raw_input("Enter count: ")
position = raw_input("Enter position: ")

currentCount = 0
currentPosition = 1

print("Retrieving: " + url)

while currentCount < 4:
    for tag in tags:
        if currentPosition == int(position):
            followMe = tag.get('href', None)
            print("Retrieving: " + followMe)
            html = urllib.urlopen(followMe).read()
            soup = BeautifulSoup(html)
            tags = soup('a')
        currentPosition += 1
currentCount += 1








    if position == 3:
        print tag.contents[0]

    num = int(tag.contents[0])
'''
