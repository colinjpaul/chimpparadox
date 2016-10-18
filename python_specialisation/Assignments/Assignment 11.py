import re

hand = open('C:\\users\\paulc1\\Documents\\GitHub\\chimpparadox\\testfiles\\regex_sum_42.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    numFound = re.findall('[0-9]+', line)

    if len(numFound) < 1:
        continue
        
    for num in numFound:
        print num
        numlist.append(num)

print numlist

print 'Maximum:', max(numlist)
