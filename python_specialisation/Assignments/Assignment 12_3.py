import urllib
from BeautifulSoup import *

#  Course requires you use file copied to local directory
#  For all other purposes 'import bs4'

#url = raw_input('Enter URL: ')

url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')

count = raw_input("Enter count: ")
position = raw_input("Enter position: ")

currentCount = 0
currentPosition = 1

print("Retrieving: " + url)

for tag in tags:
    print("Retrieving: " + tag.get('href', None))

    if currentPosition == int(position):
        followMe = tag.get('href', None)

        html = urllib.urlopen(followMe).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        print tags




    currentPosition += 1

    '''if position == 3:
        print tag.contents[0]

    num = int(tag.contents[0])'''


