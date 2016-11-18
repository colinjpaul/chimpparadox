import urllib
from BeautifulSoup import *

#  Course requires you use file copied to local directory
#  For all other purposes 'import bs4'

#url = raw_input('Enter URL: ')
url = 'http://python-data.dr-chuck.net/known_by_Leilan.html'

currentCount = 0
count = raw_input("Enter count: ")
count = int(count)

position = raw_input("Enter position: ")
position = int(position)
position -= 1

print('Retrieving: ' + url)

while currentCount < count:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    tag = tags[position]
    url = tag.get('href', None)
    print ('Retrieving: ' + url)
    currentCount += 1

