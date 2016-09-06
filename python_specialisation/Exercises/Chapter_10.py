fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "C://Users//cjadmin//Documents//GitHub//chimpparadox//testfiles/romeo.txt"
fhand = open(fname)

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print counts

lst = list()

for key, val in counts.items():
    lst.append((val, key))


lst.sort(reverse=True)

print lst

#continue from 12:21 in video
'''

for val, key in lst[:10]:
    print key, val


# Shorter version

c = {'a': 10, 'b': 1, 'c': 22}

print sorted([(v, k) for k, v in c.items()])

'''
