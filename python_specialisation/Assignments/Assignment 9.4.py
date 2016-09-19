name = raw_input("Enter file:")
if len(name) < 1 : name = "C:\\users\\paulc1\\Documents\\GitHub\\chimpparadox\\testfiles\\mbox-short.txt"
handle = open(name)
counts = dict()

bigCount = None
mostProfilic = None

for line in handle:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()

    if len(words[0]) == 4:
        counts[words[1]] = counts.get(words[1], 0) + 1
        for word, count in counts.items():
            if bigCount is None or count > bigCount:
                mostProfilic = word
                bigCount = count

print mostProfilic, bigCount
























#print 'Count of words', counts


#print "There were", count, "lines in the file with From as the first word"

#print linelist