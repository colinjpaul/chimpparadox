fname = raw_input("enter filename: ")
try:
    fhand = open(fname)
except:
    print 'file not found'
    exit()

count = 0
for line in fhand:
    if line.startswith('From:'):
        count += 1

print count
