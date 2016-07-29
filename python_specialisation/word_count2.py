counts = dict()

filehandle = open("C:\\users\\cjadmin\\Documents\\GitHub\\chimpparadox\\testfiles\\clownandcar.txt")

for line in filehandle:
    words = line.split()
    print 'Words: ', words
    print 'Counting...'

    for word in words:
        counts[word] = counts.get(word, 0) + 1


print 'Count of words', counts



