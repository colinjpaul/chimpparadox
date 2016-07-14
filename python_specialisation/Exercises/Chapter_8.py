
fhand = open('C:\\Users\\paulc1\\Documents\\GitHub\\chimpparadox\\testfiles\\mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print words[1]



# continue from 24:23 in Chapter 8, lists



