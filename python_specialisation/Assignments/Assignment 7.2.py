# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sppos = line.find(' ')
    number = float(line[sppos:])
    count += 1
    total += number
    #print line
#print "Done"
average = total/count
print "Average spam confidence:", average
