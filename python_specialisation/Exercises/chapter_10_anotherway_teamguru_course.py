fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = r"C:\Users\paulc1\Documents\GitHub\chimpparadox\testfiles\romeo.txt"
fhand = open(fname)

all_text = fhand.read()
all_text.replace('\n', ' ')

words = all_text.split(' ')

from collections import Counter

output = Counter(words)

print output

'''
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#print counts

lst = list()
for key, val in counts.items():
    lst.append((val, key))

print lst

'''