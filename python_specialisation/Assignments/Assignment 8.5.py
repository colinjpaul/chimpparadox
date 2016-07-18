fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "C://Users//paulc1//Documents//GitHub//chimpparadox//testfiles//mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From'): continue
    linelist = line.split()

    if len(linelist[0]) == 4:
        count = count + 1
        print linelist[1]

print "There were", count, "lines in the file with From as the first word"