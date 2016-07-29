
fhand = open('C:\\users\\cjadmin\\Documents\\GitHub\\chimpparadox\\testfiles\\mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]

    pieces = email.split('@')
    print pieces[1]

t = [9, 41, 12, 3, 74, 15]
print t[2:4]

friends = [ 'Joseph', 'Glenn', 'Sally']
friends.sort()
print friends[0]


#Continue from Assignment 8.4



