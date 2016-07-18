fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    print line.rstrip()
    words = line.split()
    for word in words:
        if word in lst:continue
        lst.append(word)

lst.sort()
print lst








