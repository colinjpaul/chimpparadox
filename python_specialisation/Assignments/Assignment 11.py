import re

hand = open('C:\\users\\paulc1\\Documents\\GitHub\\chimpparadox\\testfiles\\regex_sum_271851.txt')
total = 0

for line in hand:
    line = line.rstrip()
    numFound = re.findall('[0-9]+', line)
    if len(numFound) < 1:
        continue
    for num in numFound:
        total += int(num)

print total

'''

Optional: Just for Fun
There are a number of different ways to approach this problem. While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this program using list comprehension:

import re
print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

Please don't waste a lot of time trying to figure out the shortest solution until you have completed the homework. List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.

'''